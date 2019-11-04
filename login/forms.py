from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class Cadastro(UserCreationForm):
  first_name = forms.CharField(
    max_length= 30, required= True, help_text= 'Required',
    widget = forms.TextInput(attrs = {'placeholder': 'Nome'}))

  last_name = forms.CharField(
    max_length= 30, required= False, help_text= 'Opitional',
    widget = forms.TextInput(attrs = {'placeholder': 'Sobrenome'}))

  email = forms.EmailField(
    max_length=254, required=True, 
    help_text ='Required. Inform a valid email address.',
    widget = forms.TextInput(attrs = {'placeholder': 'Email'}))

  user_ra = forms.CharField(
    max_length= 30,  required= True, help_text='Required',
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
    max_length= 30, required= True, help_text= 'Required',
    widget = forms.TextInput(attrs = {'placeholder': 'Nome'}))

  last_name = forms.CharField(
    max_length= 30, required= False, help_text= 'Opitional',
    widget = forms.TextInput(attrs = {'placeholder': 'Sobrenome'}))
  
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
    max_length= 30,  required= True, help_text='Required',
    label = 'RA', error_messages='')

  user_course = forms.ChoiceField(
    choices= Profile.COURSE_CHOISES, label = 'Curso')
  
  class Meta:
    model = Profile
    fields =(
    'user_ra',
    'user_course',
    )
