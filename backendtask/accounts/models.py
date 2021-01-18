from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Favourite(models.Model):
    category = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.category


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=200,null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=False)
    favourites = models.ManyToManyField(Favourite,blank=True)
    def __str__(self):
        return self.email


