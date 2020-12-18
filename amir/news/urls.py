from django.urls import path

from . import views

urlpatterns=[
    path('scrape/',views.scrape,name="scrape"),
    path('playlist/',views.current,name="current"),
    path('home/',views.news_list,name="home"),
    
    
]