from django.urls import path
from . import views

urlpatterns = [
    path('', views.feedback, name='feedback'),
    path('success/', views.feedback_success, name='feedback_success'),
]
