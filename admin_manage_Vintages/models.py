from django.db import models
from admin_manage_producer.models import AwSetTo
import django
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class AwVintages(models.Model):
    Vintages_Year = models.IntegerField(unique=True,default=0)
    Set_To = models.ManyToManyField(AwSetTo, blank=True, related_name='AwVintages_set_to')
    Status = models.BooleanField(default=True)
    Created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='AwVintages_Created_by')
    Created_date = models.DateTimeField(default=django.utils.timezone.now)
    Updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name='AwVintages_Updated_by')
    Updated_date = models.DateTimeField(default=django.utils.timezone.now)


    def __str__(self):
        return str(self.Vintages_Year)
    class Meta:
        verbose_name_plural = "Aw Vintages"


    def get_absolute_url(self):
        return reverse('admin_manage_Vintages:vintages')