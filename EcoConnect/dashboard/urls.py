from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    # Main Dashboard Home
    path('', views.dashboard_home, name='dashboard_home'),

    # Product Management
    path('products/', views.dashboard_products_list, name='products_list'),
    path('products/add/', views.dashboard_add_product, name='add_product'),
    path('products/edit/<int:product_id>/', views.dashboard_edit_product, name='edit_product'),
    path('products/delete/<int:product_id>/', views.dashboard_delete_product, name='delete_product'),

    # User Management
    path('users/', views.dashboard_users_list, name='users_list'),

    # Orders Management
    path('orders/', views.dashboard_orders_list, name='orders_list'),

    # Complaints Management
    path('complaints/', views.dashboard_complaints_list, name='complaints_list'),

    # News Management
    path('news/', views.dashboard_news_list, name='news_list'),
    path('news/add/', views.dashboard_add_news, name='add_news'),
    path('news/edit/<int:news_id>/', views.dashboard_edit_news, name='edit_news'),
    path('news/delete/<int:news_id>/', views.dashboard_delete_news, name='delete_news'),

    # Initiatives Management
    path('initiatives/', views.dashboard_initiatives_list, name='initiatives_list'),
    path('initiatives/add/', views.dashboard_add_initiative, name='add_initiative'),
    path('initiatives/edit/<int:init_id>/', views.dashboard_edit_initiative, name='edit_initiative'),
    path('initiatives/delete/<int:init_id>/', views.dashboard_delete_initiative, name='delete_initiative'),

    # Feedback Management
    path('feedback/', views.dashboard_feedback_list, name='feedback_list'),
]
