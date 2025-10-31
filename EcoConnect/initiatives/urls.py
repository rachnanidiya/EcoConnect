from django.contrib import admin
from django.urls import include, path
from initiatives import views

urlpatterns = [
    path('',views.initiatives_list,name='initiatives_list'),
    path('<int:id>/',views.initiative_detail,name='initiative_detail'),
    
]