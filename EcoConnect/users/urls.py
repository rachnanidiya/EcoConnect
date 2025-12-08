from django.contrib import admin
from django.urls import include, path
from users import views

urlpatterns = [
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.logout_view,name='logout'),
    path("address/add/", views.add_address, name="add_address"),
    path("address/edit/<int:id>/", views.edit_address, name="edit_address"),
    path("address/delete/<int:id>/", views.delete_address, name="delete_address"),
]