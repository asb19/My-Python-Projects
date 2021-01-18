from django.contrib import admin

# Register your models here.
from .models import Favourite,UserProfile

admin.site.register(Favourite)
admin.site.register(UserProfile)
