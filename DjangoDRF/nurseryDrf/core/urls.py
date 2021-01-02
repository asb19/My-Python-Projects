from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.getPlants, name='plantlist'),
    path('addplantitem', views.addPlants, name='plantadd'),
    path('addtoorder/<int:pk>', views.add_to_cart, name='cartadd'),
    path('orderList', views.viewOrders, name='orders'),
]