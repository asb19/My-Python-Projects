from django.db import models
from django.urls import reverse

# Create your models here.

class Wallpapers(models.Model):
    title=models.TextField(max_length=20)
    image=models.ImageField(upload_to='wallpaper_image')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail",kwargs={"id":self.id})

    