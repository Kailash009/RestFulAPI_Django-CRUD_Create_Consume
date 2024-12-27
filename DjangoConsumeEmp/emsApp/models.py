from django.db import models

# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    mobileno=models.CharField(max_length=20)
    city=models.CharField(max_length=50)
    salary=models.FloatField()
    def __str__(self):
        return self.name
