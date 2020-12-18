from django.urls import path

from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('destinations/<int:dest_id>',views.destinations,name="destinations"),
    path('search',views.search,name='search'),
    path('tell',views.tell,name="tell"),
    path('page1',views.page1,name="page1"),
    path('series',views.series,name="series"),
    path('page3',views.page3,name="page3"),
    path('home',views.home,name="home"),
    path('analyzer',views.analyzer,name="analyzer"),
    path('navigator',views.nav,name="nav"),
    path('about',views.about,name="about"),
    path('destination/create',views.destination_create,name="createDest"),

]