from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=200)
    age =  models.IntegerField('Age')
    joining_date = models.DateTimeField('Joining date')
    salary = models.IntegerField('salary')
    role = models.CharField(max_length=200)
    performance_persent = models.IntegerField(default=0)
