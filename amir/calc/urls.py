from django.urls import path

from . import views

urlpatterns=[
    path('',views.home,name=""),
    path('enq',views.getData,name=""),
    path('add',views.add,name="add")
]