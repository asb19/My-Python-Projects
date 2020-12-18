from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import destination
from .models import newspost

# Register your models here.
class DestinationAdmin(admin.ModelAdmin):
    list_display=('name','updated','timestamp','price')
    list_display_links=None
    list_filter=['updated','price']
    list_editable=['price']
    search_fields=['desc']
    class Meta:
        model=destination
    

admin.site.register(destination,DestinationAdmin)
admin.site.register(newspost)
