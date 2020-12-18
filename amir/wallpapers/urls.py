from django.urls import path

from . import views

urlpatterns=[
    path('',views.wallpaper,name="list"),
    path('create',views.create_wallpaper,name="create"),
    path('wallpaper/<id>',views.detail_wallpaper,name="detail"),
    path('wallpaper/<id>/delete',views.delete_wallpaper,name="delete"),
   

]