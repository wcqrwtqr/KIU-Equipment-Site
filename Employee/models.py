from django.db import models
from django.urls import reverse
# Create your models here.


class EmployeeDB(models.Model):
    OSID = models.IntegerField(unique=True,blank=False)
    first_name = models.CharField(max_length=255,blank=False)
    last_name = models.CharField(max_length=255,blank=False)
    nationality = models.CharField(max_length=255,blank=True,default='Iraq')
    position = models.CharField(max_length=255,blank=True)
    isExpat = models.BooleanField(default=False)
    isEmployee = models.BooleanField(default=True)
    rotation = models.CharField(max_length= 10, default='5x5',blank=True)
    BU = models.CharField(max_length= 3, default='KIU')
    BL = models.CharField(max_length= 3, default='SWT')
    grade = models.IntegerField(blank=True,default=8)

    def get_absolute_url(self):
        return revere('employee_detail',kwargs={'pk':self.pk})

    def __str__(self):
        return '%s %s'% (self.first_name, self.last_name)

