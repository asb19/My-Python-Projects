from django.contrib import admin
from .models import todoitems,todo_user

# Register your models here.
admin.site.register(todoitems)
admin.site.register(todo_user)



