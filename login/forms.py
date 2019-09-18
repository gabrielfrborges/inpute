from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Cadastro(UserCreationForm):
    first_name = forms.CharField(max_length= 30, required= False, help_text= 'Opitional')
    last_name = forms.CharField(max_length= 30, required= False, help_text= 'Opitional')
    email = forms.EmailField(max_length=254, required=True, help_text ='Required. Inform a valid email address.')
    user_ra = forms.CharField(max_length= 30,  required= True, help_text='Required', label = 'RA', error_messages='')
    USER_COURSES_CHOICES = [
      (1, 'Analise e Desenvolvimento de sistemas'),
      (2, 'Banco de dados'),
      (3, 'Gestão da Produção Industrial'),
      (4, 'Logística'),
      (5, 'Manutafura Avançada'),
      (6, 'Manutafura e Aeronaves'),
      (7, 'Projetos de Estruturas Aeronáuticas')
    ]
    user_course = forms.ChoiceField(choices = USER_COURSES_CHOICES, widget = forms.RadioSelect, label= 'Curso')

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