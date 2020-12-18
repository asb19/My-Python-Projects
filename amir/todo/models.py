from django.db import models
from django.conf import settings

# Create your models here.

class todoitems(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,default=None,on_delete=models.PROTECT)
    content=models.TextField()
    def __str__(self):
        return self.content[:10]
    
class todo_user(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=12)
    
    
