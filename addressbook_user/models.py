from django.db import models
from django.contrib.auth.models import User
import django
from admin_manage_setting.models import AwManageShipping
# Create your models here.
class AwAddressBook(models.Model):
    User = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='User_Address')
    First_Name = models.CharField(max_length=120)
    Last_Name = models.CharField(max_length=120)
    Email = models.CharField(max_length=120)
    Pnone_no = models.IntegerField(default=0)
    Conpany_Name = models.CharField(max_length=120,null=True,blank=True)
    Country = models.ForeignKey(AwManageShipping, on_delete=models.SET_NULL, null=True, blank=True, related_name='country_Address')
    Address = models.TextField()
    Address_2 = models.TextField(null=True,blank=True)
    City = models.CharField(max_length=120)
    State = models.CharField(max_length=120,default="" ,null=True,blank=True)
    Postcode = models.IntegerField(default=0)
    Landmark = models.CharField(max_length=120,null=True,blank=True)
    Create_Date = models.DateTimeField(default=django.utils.timezone.now)
    Update_Date = models.DateTimeField(default=django.utils.timezone.now)


    def __str__(self):
        return str(self.Address)
    class Meta:
        verbose_name_plural = "AW Address Book"


