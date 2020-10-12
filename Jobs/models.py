from django.db import models
from django.urls import reverse
# Create your models here.

class JobsDB(models.Model):
    JOBID = models.CharField(max_length = 20 ,unique=True,blank=False)
    client = models.CharField(max_length=255,blank=False)
    field = models.CharField(max_length=255,blank=True)
    well = models.CharField(max_length=255,blank=False)
    country = models.CharField(max_length=255,blank=False,default='Iraq')
    BU = models.CharField(max_length= 3, default='KIU')
    BL = models.CharField(max_length= 3, default='SWT')
    description = models.CharField(max_length= 800, blank=True)
    isContract = models.BooleanField(default=True)
    startDate = models.DateField(null=True)
    endDate = models.DateField(blank=True,null=True)


    def __str__(self):
        return '%s %s %s'% (self.JOBID, self.client, self.well)


