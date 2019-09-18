from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import Cadastro
# Create your views here.

def cadastro(request):
    if request.method == 'POST':
        form = Cadastro(request.POST)
        if form.is_valid():
            form.save()
            user.fresh_from_db()
            user.profile.user_ra = form.cleaned_data.get('user_ra')
            #user.profile.user_course = form.cleaned_data.get('user_course')
            user.save()
            username = form.cleaned_data.get('username')
            raw_passoword = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = raw_password)
            login(request,user)
            return redirect('home')
    else:
        form = Cadastro()
    return render(request, 'login/cadastro.html', {'form': form})

def home(request):
    return render(request, 'login/home.html')
