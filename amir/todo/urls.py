from django.urls import path

from . import views

urlpatterns=[
    path('todolist',views.todolist,name="todolist"),
    path('addtodo',views.addtodo,name="addtodo"),
    path('deleteTask/<int:item_id>',views.deleteTask,name="deleteTask"),
    path('register',views.register,name="register"),
    path('register_task',views.register_task,name="register_task"),
    path('login',views.login_todo,name="login"),
    path('todo_login',views.todo_login,name="todo_login"),
    path('logout',views.logout,name="logout"),
    
]