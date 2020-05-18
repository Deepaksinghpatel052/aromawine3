from django.db import models
from admin_manage_producer.models import AwSetTo
from admin_manage_country.models import AwCountry
from datetime import date
import django
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.




class AwAppellation(models.Model):
    Appellation_Name = models.CharField(max_length=120,unique=True)
    Country = models.ManyToManyField(AwCountry, blank=True, related_name='AwAppellation_country')
    Set_To = models.ManyToManyField(AwSetTo, blank=True, related_name='AwAppellation_set_to')
    Status = models.BooleanField(default=True)
    Created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='AwAppellation_Created_by')
    Created_date = models.DateTimeField(default=django.utils.timezone.now)
    Updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name='AwAppellation_Updated_by')
    Updated_date = models.DateTimeField(default=django.utils.timezone.now)


    def __str__(self):
        return str(self.Appellation_Name)
    class Meta:
        verbose_name_plural = "AW Appellation"


    def get_absolute_url(self):
        return reverse('admin_manage_appellation:appellation')