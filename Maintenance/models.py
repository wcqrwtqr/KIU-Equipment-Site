from django.db import models
from django.urls import reverse
from FAR.models import FAR_DB
# Create your models here.

class MaintenanceDB(models.Model):
    main_date_start = models.DateField( null=True)
    ms_type= models.CharField(max_length=20, null=True)
    main_date_end = models.DateField(blank=True, null=True)
    main_cost = models.DecimalField(max_digits=8, null=True,decimal_places=2,blank=True)
    expiry_date = models.DateField(blank=True, null=True)
    asset = models.ForeignKey(FAR_DB,on_delete=models.CASCADE)
    description = models.CharField(max_length=900, null=True,blank=True)


    def get_absolute_url(self):
        return reverse ('maintenance_detail',kwargs={'pk':self.pk})


    def __str__(self):
        return '%s %s %s' % (self.ms_type,self.main_date_start,self.asset)











