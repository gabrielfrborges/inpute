from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class Cadastro(UserCreationForm):
  first_name = forms.CharField(
    max_length= 30, required= True, help_text= 'Obrigatório',
    widget = forms.TextInput(attrs = {'placeholder': 'Nome'}))

  last_name = forms.CharField(
    max_length= 30, required= False, help_text= 'Opcional',
    widget = forms.TextInput(attrs = {'placeholder': 'Sobrenome'}))

  email = forms.EmailField(
    max_length=254, required=True, 
    help_text ='Obrigatório',
    widget = forms.TextInput(attrs = {'placeholder': 'Email'}))

  user_ra = forms.CharField(
    max_length= 30,  required= True, help_text='Obrigatório',
    label = 'RA', error_messages='')

  user_course = forms.ChoiceField(
    choices= Profile.COURSE_CHOISES, label = 'Curso')

  is_monitor = forms.CheckboxInput()

  class Meta:
    model= User
    fields = (
    'username', 
    'first_name', 
    'last_name', 
    'email', 
    'password1', 
    'password2',
    'user_ra',
    'user_course',
    )
    exclude = [
      'is_monitor'
    ]

class UserUpdateForm(forms.ModelForm):
  first_name = forms.CharField(
    max_length= 30, required= True, 
    widget = forms.TextInput(attrs = {'placeholder': 'Nome obrigatório', 'class': 'form-control'}))

  last_name = forms.CharField(
    max_length= 30, required= False,
    widget = forms.TextInput(attrs = {'placeholder': 'Sobrenome opcional', 'class': 'form-control'}))
  
  class Meta:
    model = User
    exclude = [
      'password',
      'username',
      'email',
      'is_monitor',
    ]
    fields = (
    'first_name', 
    'last_name',
    )

class ProfileUpdateForm(forms.ModelForm):
  user_ra = forms.CharField( 
    widget = forms.TextInput(attrs= {'class': 'form-control'}),
    max_length= 30,  required= True, 
    label = 'RA', error_messages='')

  user_course = forms.ChoiceField(
    widget = forms.Select(attrs={'class': 'form-control'}),
    choices= Profile.COURSE_CHOISES, label = 'Curso')
  
  class Meta:
    model = Profile
    fields =(
    'user_ra',
    'user_course',
    )
