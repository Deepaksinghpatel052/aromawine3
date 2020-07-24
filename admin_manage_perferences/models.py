from django.db import models
from django.contrib.auth.models import User
import django
from django.urls import reverse
from admin_manage_products.models import AwProducts,AwProductPrice
from addressbook_user.models import AwAddressBook
from wineproject.utils import  unique_id_generator_for_order
from django.db.models.signals import pre_save

# Create your models here.

class AwInterestType(models.Model):
    Type = models.CharField(max_length=120,unique=True)
    Status = models.BooleanField(default=True)
    Created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name='AwInterestType_Created_by')
    Created_date = models.DateTimeField(default=django.utils.timezone.now)
    Updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name='AwInterestType_Updated_by')
    Updated_date = models.DateTimeField(default=django.utils.timezone.now)

    def get_absolute_url(self):
        return reverse('admin_manage_perferences:perferences')
    def __str__(self):
        return str(self.Type)

    class Meta:
        verbose_name_plural = "Aw Interest Type"



class Service_Interests(models.Model):
    Service_interests_name = models.CharField(max_length=120)
    Select_Type = models.ForeignKey(AwInterestType, on_delete=models.SET_NULL, null=True, blank=True,related_name='AwServiceInterests_Created_by')
    Date = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return str(self.Service_interests_name)

    class Meta:
        verbose_name_plural = "Aw Service Interests"


