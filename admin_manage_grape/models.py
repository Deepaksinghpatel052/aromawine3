from MarkupPy.markup import _oneliner
from django.db import models
from datetime import date
import django
from django.urls import reverse
from django.contrib.auth.models import User
from wineproject.utils import  slug_generator_for_AwGrape
from django.db.models.signals import pre_save
# Create your models here.

def user_directory_path(instance, filename):
    producer_id_in_list = instance.Grape_Name.split(" ")
    today_date = date.today()
    producer_id_in_string = '_'.join([str(elem) for elem in producer_id_in_list])
    return '{0}/{1}'.format(producer_id_in_string+"/Grape/"+str(today_date.year)+"/"+str(today_date.month)+"/"+str(today_date.day),filename)

def user_directory_path_banner(instance, filename):
    producer_id_in_list = instance.Grape_Name.split(" ")
    today_date = date.today()
    producer_id_in_string = '_'.join([str(elem) for elem in producer_id_in_list])
    return '{0}/{1}'.format(producer_id_in_string+"/Grape/banner/"+str(today_date.year)+"/"+str(today_date.month)+"/"+str(today_date.day),filename)

class AwGrape(models.Model):
    Grape_Name = models.CharField(max_length=120,unique=True)
    Slug = models.CharField(max_length=120, unique=True, null=True, blank=True)
    Grape_Image = models.ImageField(upload_to=user_directory_path)
    Grape_banner_Image = models.ImageField(upload_to=user_directory_path_banner,null=True, blank=True)
    Description = models.TextField(null=True, blank=True)
    Status = models.BooleanField(default=True)
    Created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name='AwGrape_Created_by')
    Created_date = models.DateTimeField(default=django.utils.timezone.now)
    Updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name='AwGrape_Updated_by')
    Updated_date = models.DateTimeField(default=django.utils.timezone.now)


    def get_absolute_url(self):
        return reverse('admin_manage_grape:grape')
    def __str__(self):
        return str(self.Grape_Name)

    class Meta:
        verbose_name_plural = "AW Grape"

def pre_save_create_slug(sender, instance, *args, **kwargs):
    if not instance.Slug:
        instance.Slug= slug_generator_for_AwGrape(instance)
pre_save.connect(pre_save_create_slug, sender=AwGrape)