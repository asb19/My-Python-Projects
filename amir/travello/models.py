from django.db import models
from django.urls import reverse

# Create your models here.
class destination(models.Model):
    
    price=models.IntegerField(default=0)
    desc=models.TextField()
    img=models.ImageField(upload_to='pics')
    name=models.CharField(max_length=50)
    offer=models.BooleanField(default=False)
    timestamp=models.DateTimeField(auto_now=False, auto_now_add=True)
    updated=models.DateTimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('destinations',kwargs={'dest_id':self.id})
        # return 'destinations/%s'%(self.id)
    

class newspost(models.Model):
    catg="Lifestyle and Travel"
    
    title=models.CharField(max_length=10)
    text=models.TextField()
    date=models.DateField(null=True,blank=False)
    month=models.CharField(max_length=10)
    img=models.ImageField(upload_to='pics')
    