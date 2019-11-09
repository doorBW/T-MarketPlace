from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here
def index(req):
    return render(req, 'index.html')

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            user.save()
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
