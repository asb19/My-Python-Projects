from django.db import models

# Create your models here.
class Employees(models.Model):
    emp_fname = models.CharField(max_length=10)
    emp_sname = models.CharField(max_length=10)
    emp_id = models.IntegerField()

    def __str__(self):
        return self.emp_fname
