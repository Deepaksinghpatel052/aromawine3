from django.db import models
from admin_manage_producer.models import AwSetTo
import django
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse
from wineproject.utils import  slug_generator_for_AwCountry
from django.db.models.signals import pre_save
# Create your models here.



def user_directory_path(instance, filename):
    producer_id_in_list = instance.Country_Name.split(" ")
    today_date = date.today()
    producer_id_in_string = '_'.join([str(elem) for elem in producer_id_in_list])
    return '{0}/{1}'.format(producer_id_in_string+"/country/"+str(today_date.year)+"/"+str(today_date.month)+"/"+str(today_date.day),filename)


def user_directory_path_banner(instance, filename):
    producer_id_in_list = instance.Country_Name.split(" ")
    today_date = date.today()
    producer_id_in_string = '_'.join([str(elem) for elem in producer_id_in_list])
    return '{0}/{1}'.format(producer_id_in_string+"/country/banner/"+str(today_date.year)+"/"+str(today_date.month)+"/"+str(today_date.day),filename)


class AwCountry(models.Model):
    Country_Name = models.CharField(max_length=120, unique=True)
    Slug = models.CharField(max_length=120, unique=True, null=True, blank=True)
    Set_To = models.ManyToManyField(AwSetTo, blank=True, related_name='AwCountry_set_to')
    Country_Image = models.ImageField(upload_to=user_directory_path,blank=True,null=True,default='default/default_country_image.jpg')
    Banner_Image = models.ImageField(upload_to=user_directory_path_banner,blank=True,null=True)
    Description = models.TextField(null=True, blank=True)
    Short_Description = models.TextField(null=True, blank=True)
    Status = models.BooleanField(default=True)
    Created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='AwCountry_Created_by')
    Created_date = models.DateTimeField(default=django.utils.timezone.now)
    Updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name='AwCountry_Updated_by')
    Updated_date = models.DateTimeField(default=django.utils.timezone.now)


    def __str__(self):
        return str(self.Country_Name)

    class Meta:
        verbose_name_plural = "AW Country"


    def get_absolute_url(self):
        return reverse('admin_manage_country:country')

def pre_save_create_slug(sender, instance, *args, **kwargs):
    if not instance.Slug:
        instance.Slug= slug_generator_for_AwCountry(instance)
pre_save.connect(pre_save_create_slug, sender=AwCountry)

class AwCountryUser(models.Model):
    Country_Name = models.CharField(max_length=120, unique=True)
    Code = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return str(self.Country_Name)

    class Meta:
        verbose_name_plural = "AW Country For Users"


