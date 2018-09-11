from django.db import models
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver

# Create your models here.
class Location(models.Model):
    name=models.CharField(max_length=20,verbose_name='Location Name')
    deleted=models.IntegerField(default=0,max_length=1)

    def __str__(self):
        return self.name

class Designation(models.Model):
    name=models.CharField(max_length=20,verbose_name='Designation Name')
    deleted=models.IntegerField(default=0,max_length=1)

    def __str__(self):
        return  self.name


class EmployeeManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(age=24)

    def get_all(self):
        return  super().get_queryset()

class Employee(models.Model):
    name=models.CharField(max_length=50,verbose_name='Employee Name')
    email=models.EmailField(primary_key=True,max_length=100,blank=False,verbose_name='Email-Id')
    mobile=models.IntegerField(max_length=10,blank=False,verbose_name='Mobile')
    location=models.ForeignKey(Location,on_delete=models.CASCADE)
    designation=models.ForeignKey(Designation,on_delete=models.CASCADE)
    age=models.IntegerField(verbose_name='Age',default=0)
    emp_object=EmployeeManager()

    def __str__(self):
        return self.name



