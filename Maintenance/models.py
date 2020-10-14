from django.db import models
from django.urls import reverse
from FAR.models import FAR_DB
# Create your models here.

class MaintenanceDB(models.Model):
    main_date_start = models.DateField()
    ms_type= models.CharField(max_length=20)
    main_date_end = models.DateField(blank=True)
    main_cost = models.DecimalField(max_digits=5,decimal_places=2,blank=True)
    expiry_date = models.DateField(blank=True)
    asset = models.ForeignKey(FAR_DB,on_delete=models.CASCADE)


    def get_absolute_url(self):
        return reverse ('maintenance_detail',kwargs={'pk':self.pk})


    def __str__(self):
        return '%s %s %s' % (self.ms_type,self.main_date_start,self.asset)











