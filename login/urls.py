from django.urls import path, include
from login.views import cadastro, home, ProfileView, profile_update
from django.views.generic.base import TemplateView
urlpatterns = [

    path('', include('django.contrib.auth.urls')),

    path('cadastro/', cadastro, name= 'cadastro'),

    path('perfil/<int:pk>', ProfileView.as_view(
        template_name = 'login/profile_detail.html'), name= 'perfil' ),

    path('perfil/edit', profile_update, name= 'perfil_edit'),

]
