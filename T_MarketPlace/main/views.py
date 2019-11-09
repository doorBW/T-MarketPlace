from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Market, Festival, Profile
from django.http import HttpResponse
from .models import Market, Festival
from .forms import MarketForm, FestivalForm

import json
import requests
from time import sleep
# Create your views here

# 메인 페이지
def index(req):
    markets = Market.objects.all()
    festivals = Festival.objects.all()
    return render(req, 'index.html', {'markets': markets, 'festivals': festivals})
# 로그인 기능
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
            # profile_data 저장
            new_profile = Profile()
            new_profile.user = user 
            new_profile.upload_date = timezone.datetime.now()
            new_profile.image = request.FILES['img1']
            new_profile.files = request.FILES['file1']
            new_profile.save()
            # 유저 아이디 및 비밀번호 저장
            user.save()
            auth.login(request, user)
            return redirect('index')
    return render(request, './signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('index')


# 시장 및 축제 페이지
def market_detail(req, market_id):
    market_detail = get_object_or_404(Market, pk=market_id)
    return render(req, 'market_detail.html', {'market': market_detail})


def festival_detail(req, festival_id):
    festival_detail = get_object_or_404(Festival, pk=festival_id)
    return render(req, 'festival_detail.html', {'festival': festival_detail})


def market_new(req):
    if req.method == 'POST':
        mk = Market(name=req.POST['name'], address=req.POST['address'], latitude=req.POST['latitude'],
                    longitude=req.POST['longitude'], url=req.POST['url'], open_day=req.POST['open_day'], content=req.POST['content'])
        mk.photo = req.FILES['photo']
        mk.save()
        return redirect('index')
    else:
        return render(req, 'newMarket.html')


def festival_new(req):
    if req.method == 'POST':
        form = FestivalForm(req.POST, req.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_at = timezone.now()
            post.save()
            return redirect('index')
    else:
        form = FestivalForm()
        return render(req, 'newFestival.html', {'form': form})

# 메인 페이지 지도랑 사진 ajax
def market_click_ajax_event(req):
    sleep(2)
    market_id = req.POST.get('market_id')
    market = Market.objects.get(id=market_id)
    print('##############', market.longitude)
    res = {'message': 'success',
           'name': market.name,
           'photo': market.photo.url,
           'open_day': market.open_day,
           'address': market.address,
           'latitude': market.latitude,
           'longitude': market.longitude}
    res = json.dumps(res)
    return HttpResponse(res)

def auto_market_data_saving(req):
    data_url = "http://115.84.165.224/bigfile/iot/sheet/json/download.do?srvType=S&infId=OA-1176&serviceKind=1&pageNo=2&gridTotalCnt=330&ssUserId=SAMPLE_VIEW&strWhere&strOrderby"
    post_res = requests(data_url)
    datas = post_res["DATA"]
    insert_cnt = 0
    for data in datas:
        markets = Market.objects.filter(name=data["m_name"])
        if len(markets) > 0:
            continue
        else:
            new_market = Market()
            new_market.name = data["m_name"]
            new_market.address = data["guname"]+" "+data["m_addr"]
            new_market.latitude = data["lng"]
            new_market.longitude = data["lat"]
            new_market.save()
            insert_cnt += 1
    if insert_cnt > 0:
        message = str(insert_cnt)+'개의 데이터를 정상적으로 추가하였습니다.' 
    else:
        message = "추가된 데이터가 없습니다."
    result_res = { 'message': message}
    return result_res