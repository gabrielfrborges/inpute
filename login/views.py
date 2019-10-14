from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.http import HttpResponse
from .forms import Cadastro, UserUpdateForm, ProfileUpdateForm
from .models import Profile
from django.contrib.auth.models import User

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
            'user_course':user.profile.get_user_courses_display(),
            'full_name':user.full_name  
        }
    return render(request, 'login/home.html', {'data': data })

class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    context_object_name = 'profile'

@login_required
def profile_update(request):
    context = {
        'form_u': UserUpdateForm(instance= request.user),
        'form_p': ProfileUpdateForm(instance= request.user.profile)
    }
    return render(request, 'login/profile_edit.html', context)

    