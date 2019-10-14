from django.urls import path, include
from posts.views import (
    QuestionView, 
    QuestionCreateView,
    QuestionListView,
    add_answer,
    )


urlpatterns = [
    path('new/', QuestionCreateView.as_view(
        template_name = 'posts/post_form.html'), name= 'new_post'),

    path('<int:pk>/', QuestionView.as_view(
        template_name = 'posts/post_detail.html'), name = 'post_detail'),

    path('list/', QuestionListView.as_view(
        template_name = "posts/post_list.html"), name ='post_list'),

    path('<int:pk>/answer/', add_answer, name='add_answer'), 

]