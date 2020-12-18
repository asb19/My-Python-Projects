from django.urls import path

from . import views

urlpatterns=[
    path('',views.apiovw,name="ovw"),
    path('tasklist',views.tasksview,name="taskview"),
    path('task-detail/<int:pk>',views.taskdetail,name="taskdetail"),
    path('task-create/',views.taskcreate,name="taskcreate"),
    path('task-update/<int:pk>',views.taskupdate,name="taskupdate"),
    path('task-delete/<int:pk>',views.taskdelete,name="taskdelete"),
    
    
]