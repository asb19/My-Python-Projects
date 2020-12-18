from django.shortcuts import render

from .models import  todoitems,todo_user
from django.shortcuts import redirect
from django.contrib.auth.models import auth
from django.contrib import messages

# Create your views here.

def todo_login(request):
    return render(request,'todo/todologin.html')

def login_todo(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('todolist')
        else:
            messages.info(request,'invalid credentials')
            return redirect('todo_login')
    else:
        return render(request,'todo/todologin.html')

def logout(request):
     auth.logout(request)
     return redirect('todolist')

def register_task(request):
    usr=request.POST['username']
    pwd=request.POST['pwd']
    if todo_user.objects.filter(username=usr):
        messages.info(request,"user already exists")
        return redirect('register')
    else:
        user=todo_user(username=usr,password=pwd)
        user.save()
        return redirect('todo_login')

def register(request):
    return render(request,'todo/todo-register.html')

def todolist(request):
    if request.user.is_authenticated:

        usr=request.user
        print(usr)
        
        all_lists=usr.todoitems_set.all()
        return render(request,'todo/todolist.html',{'all_lists':all_lists})
    return redirect('todo_login')


def addtodo(request):
    content=request.POST['task']
    task=todoitems(content=content,user=request.user)
    task.save()
    return redirect('todolist')

def deleteTask(request,item_id):
    item=todoitems.objects.get(id=item_id)
    print(item)
    item.delete()
    return redirect('todolist') 


