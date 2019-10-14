from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import Cadastro
# Create your views here.

def cadastro(request):
    if request.method == 'POST':
        form = Cadastro(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.user_ra = form.cleaned_data.get('user_ra')
            user.profile.user_course = form.cleaned_data.get('user_course')
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = raw_password)
            login(request,user)
            return redirect('home')
    else:
        form = Cadastro()
    return render(request, 'login/cadastro.html', {'form': form})

@login_required 
def home(request):
    if user.is_authenticated():
        data = {
            'username':user.username,
            'user_course':user.profile.get_user_courses_display()
        }
    return render(request, 'login/home.html', {'data': data })
