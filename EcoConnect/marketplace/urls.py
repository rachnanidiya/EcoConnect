from django.urls import path
from . import views

urlpatterns = [
    path('', views.marketplace_home, name='marketplace_home'),
    path('products/', views.marketplace_products, name='marketplace_products'),
    path('product/<int:id>/', views.marketplace_product_detail, name='marketplace_product_detail'),
    path('sell/', views.marketplace_sell_item, name='marketplace_sell'),
]
