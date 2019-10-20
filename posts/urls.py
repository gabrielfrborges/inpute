"""inpute URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from posts.views import (
    QuestionView, 
    QuestionCreateView,
    QuestionListView,
    add_answer,
    change_post
    )


urlpatterns = [
    path('new/', QuestionCreateView.as_view(
        template_name = 'posts/post_form.html'), name= 'new_post'),

    path('<int:pk>/', QuestionView.as_view(
        template_name = 'posts/post_detail.html'), name = 'post_detail'),

    path('list/', QuestionListView.as_view(
        template_name = "posts/post_list.html"), name ='post_list'),

    path('<int:pk>/answer/', add_answer, name='add_answer'),

    path('<int:pk>/edit', change_post, name = 'post_edit')

]