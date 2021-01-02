from django.contrib import admin
from .models import Plant,OrderItems,Order
# Register your models here.
admin.site.register(Plant)
admin.site.register(OrderItems)
admin.site.register(Order)
