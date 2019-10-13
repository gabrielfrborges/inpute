from django.urls import path, include
from login.views import cadastro, home
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('cadastro/', cadastro, name = 'cadastro'),
]
