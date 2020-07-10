from django.db import models
from admin_manage_producer.models import AwSetTo
import django
from django.contrib.auth.models import User
from django.urls import reverse
from wineproject.utils import  slug_generator_for_AwVintages
from django.db.models.signals import pre_save
# Create your models here.

class AwVintages(models.Model):
    Vintages_Year = models.IntegerField(unique=True,default=0)
    Slug = models.CharField(max_length=120,unique=True,null=True,blank=True)
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
def pre_save_create_slug(sender, instance, *args, **kwargs):
    if not instance.Slug:
        instance.Slug= slug_generator_for_AwVintages(instance)
pre_save.connect(pre_save_create_slug, sender=AwVintages)