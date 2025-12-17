from django.urls import path
from . import views

app_name = 'forum'
urlpatterns = [
    path('', views.forum_list, name='forum_list'),
    path('new/', views.create_post, name='create_post'),
    path('<int:post_id>/', views.forum_detail, name='forum_detail'),
]
