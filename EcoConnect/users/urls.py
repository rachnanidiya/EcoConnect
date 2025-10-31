from django.contrib import admin
from django.urls import include, path
from users import views

urlpatterns = [
    path('',views.home),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
]