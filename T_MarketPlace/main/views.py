#-*- coding:utf-8 -*-
from time import sleep
import requests
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Market, Festival, Profile
from django.http import HttpResponse
from .models import Market, Festival
from .forms import MarketForm, FestivalForm
# Create your views here

# 메인 페이지


def index(req):
    markets = Market.objects.all().order_by('name')
    festivals = Festival.objects.all()
    return render(req, 'index.html', {'markets': markets, 'festivals': festivals})
# 로그인 기능


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                request.POST['username'], password=request.POST['password1'])
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
        mk.created_at = timezone.now()
        user = req.user.username
        mk.author = user

        mk.save()
        return redirect('index')
    else:
        return render(req, 'newMarket.html')


def festival_new(req):
    markets = Market.objects.all()
    if req.method == 'POST':
        fest = Festival(name=req.POST['name'], date=req.POST['date'], pay=req.POST['pay'],
                        host=req.POST['host'], address=req.POST['address'], url=req.POST['url'], content=req.POST['content'])
        fest.photo = req.FILES['photo']
        market = Market.objects.get(id=req.POST['market'])
        fest.market = market
        fest.created_at = timezone.now()
        fest.save()
        return redirect('index')
    else:
        return render(req, 'newFestival.html', {'markets': markets})


def market_update(req, market_id):
    #mk = Market.objects.get(pk=market_id)
    mk = get_object_or_404(Market, pk=market_id)
    if req.method == 'POST':
        mk.name = req.POST['name']
        mk.address = req.POST['address']
        mk.latitude = req.POST['latitude']
        mk.longitude = req.POST['longitude']
        mk.url = req.POST['url']
        mk.open_day = req.POST['open_day']
        mk.content = req.POST['content']
        mk.photo = req.FILES['photo']
        mk.created_at = timezone.now()
        user = req.user.username
        mk.author = user
        mk.save()
        return redirect('/detail/+int(market.pk)')
    else:
        return render(req, 'updateMarket.html')


def festival_update(req, festival_id):
    markets = Market.objects.all()
    festival = get_object_or_404(Festival, pk=festival_id)
    if req.method == "POST":
        fest = Festival(name=req.POST['name'], date=req.POST['date'], pay=req.POST['pay'],
                        host=req.POST['host'], address=req.POST['address'], url=req.POST['url'], content=req.POST['content'])
        fest.photo = req.FILES['photo']
        market = Market.objects.get(id=req.POST['market'])
        fest.market = market
        fest.created_at = timezone.now()
        fest.save()
        return redirect('/detail/+int(festival.pk)')
    else:
        return render(req, 'updateFestival.html', {'markets': markets})

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
    sleep(2)
    data_url = "http://115.84.165.224/bigfile/iot/sheet/json/download.do?srvType=S&infId=OA-1176&serviceKind=1&pageNo=2&gridTotalCnt=330&ssUserId=SAMPLE_VIEW&strWhere&strOrderby"
    post_res = requests.post(data_url)
    datas = json.dumps(post_res)["DATA"]
    # datas = post_res.json()["DATA"]
    # datas = json.loads(datas)
    insert_cnt = 0
    print(datas)
    for data in datas:
        markets = Market.objects.filter(name=data["m_name"])
        if len(markets) > 0:
            continue
        else:
            new_market = Market()
            new_market.name = data["m_name"]
            new_market.address = data["guname"]+" "+data["m_addr"]
            new_market.latitude = data["lat"]
            new_market.longitude = data["lng"]
            new_market.save()
            insert_cnt += 1
    if insert_cnt > 0:
        message = str(insert_cnt)+'개의 데이터를 정상적으로 추가하였습니다.'
    else:
        message = "추가된 데이터가 없습니다."
    result_res = { 'message': message}
    result_res = json.dumps(result_res)
    return HttpResponse(result_res)
