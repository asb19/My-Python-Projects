from django.urls import path

from . import views

urlpatterns=[
    path('index/',views.indexView,name="indexView"),
    path('change/',views.check,name="checkView"),
    
    
]