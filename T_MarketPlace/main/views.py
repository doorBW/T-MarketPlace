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
        form = MarketForm(req.POST, req.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_at = timezone.now()
            post.save()
            return redirect('index')
    else:
        form = MarketForm()
        return render(req, 'newMarket.html', {'form': form})


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
    market_id = req.POST.get('market_id')
    market = Market.objects.get(id=market_id)
    print('##############',market.longitude)
    res = { 'message':'success',
            'name':market.name,
            'photo':market.photo.url,
            'open_day':market.open_day,
            'address':market.address,
            'latitude':market.latitude,
            'longitude':market.longitude}
    res = json.dumps(res)
    return HttpResponse(res)
