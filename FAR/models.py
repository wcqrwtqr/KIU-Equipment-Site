from django.db import models
from  django.urls import reverse
# Create your models here.


class FAR_DB(models.Model):
    asset_num = models.CharField(max_length=200,unique=True, blank=False)
    serial_num = models.CharField(max_length=200,unique=True,blank=True)
    description = models.CharField(max_length=800)
    BU = models.CharField(max_length=4)
    BL = models.CharField(max_length=4)
    asset_life = models.IntegerField()
    acquisition_cost  = models.DecimalField(max_digits=10, decimal_places=2)
    tot_dep_value  = models.DecimalField(max_digits=10, decimal_places=2)
    nbv  = models.DecimalField(max_digits=10, decimal_places=2)
    acquisition_date  = models.DateField()
    equ_type = models.CharField(max_length=200)
    temp_location = models.CharField(max_length=200, blank=True)

    def addFar(self):
        self.save()

    def get_absolute_url(self):
        return revere('far_detail',kwargs={'pk':self.pk})

    def __str__(self):
        return '%s %s'% (self.equ_type ,self.serial_num )
