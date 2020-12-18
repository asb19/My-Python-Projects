from django.db import models

# Create your models here.
class TempValue(models.Model):
    incelcius=models.BooleanField(default=False)

class cityModel(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
