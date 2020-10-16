from django.db import models
from django.urls import reverse
from FAR.models import FAR_DB
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

    def get_absolute_url(self):
        return revere('jobs_detail',kwargs={'pk':self.pk})

    def __str__(self):
        return '%s %s %s'% (self.JOBID, self.client, self.well)


class JobMasterInfo(models.Model):
    job = models.ForeignKey(JobsDB,null=True, on_delete=models.CASCADE)
    assets = models.ManyToManyField(FAR_DB,null=True )
    h2s = models.DecimalField(max_digits=3,decimal_places=2,blank=True)
    co2 = models.DecimalField(max_digits=3,decimal_places=2,blank=True)
    oilRate = models.DecimalField(max_digits=10,decimal_places=2,blank=True)
    gasRate = models.DecimalField(max_digits=10,decimal_places=3,blank=True)
    description = models.CharField(max_length= 800, blank=True)

    def get_absolute_url(self):
        return revere('jobs_master_info',kwargs={'pk':self.pk})

    def __str__(self):
        return '%s'% (self.job )
