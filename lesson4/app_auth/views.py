from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from .forms import UserRegister

def profile_view(request):
    return render(request, 'app_auth/profile.html')

def register_view(request):
    if request.method == 'GET':
        form = UserRegister()
        return render(request, 'app_auth/register.html', {'form': form})    
   
    if request.method == 'POST':
        form = UserRegister(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'app_auth/register.html', {'form': form})

def login_view(request):
    redirect_url = reverse('profile')
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(redirect_url)
        else:
            return render(request, 'app_auth/login.html')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(redirect_url)
    return render(request, 'app_auth/login.html', {"error":'Пользователь не найден'})

def logout_view(request):
    logout(request)
    return redirect(reverse('login'))