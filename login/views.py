from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.http import HttpResponse
from .forms import Cadastro, UserUpdateForm, ProfileUpdateForm
from .models import Profile
from django.contrib.auth.models import User

# Create your views here.

def custom_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return views.login(request)

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
            'user_course':user.profile.get_user_courses_display(),
            'full_name':user.full_name  
        }
    return render(request, 'login/home.html', {'data': data })

class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    context_object_name = 'profile'

@login_required
def profile_update(request):
    if request.method == 'POST':
        form_u = UserUpdateForm(request.POST, instance= request.user)
        form_p = ProfileUpdateForm(request.POST, instance= request.user.profile)
        if form_u.is_valid() and form_p.is_valid():
            form_u.save()
            form_p.save()
            return redirect('my_profile')
    else:
        context = {
            'form_u': UserUpdateForm(instance= request.user),
            'form_p': ProfileUpdateForm(instance= request.user.profile)
        }
        return render(request, 'login/profile_edit.html', context)

@login_required
def my_profile(request):
    return redirect('perfil', pk= request.user.pk)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.POST, instance = request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('my_perfil')
    else:
        form = PasswordChangeForm(request.user)
        context = {'form': form}
        return render(request, 'login/profile_password.html', context)

