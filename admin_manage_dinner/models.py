from django.db import models
import django
from datetime import date
from django.contrib.auth.models import User
from django.urls import reverse
from wineproject.utils import  slug_generator_for_AAwDinner
from django.db.models.signals import pre_save
from admin_manage_products.models import AwProducts

# Create your models here.


def user_directory_path(instance, filename):
    producer_id_in_list = instance.Dinner_Name.split(" ")
    today_date = date.today()
    producer_id_in_string = '_'.join([str(elem) for elem in producer_id_in_list])
    return '{0}/{1}'.format(producer_id_in_string+"/Dinner/"+str(today_date.year)+"/"+str(today_date.month)+"/"+str(today_date.day),filename)


class AwDinner(models.Model):
    Dinner_Name = models.CharField(max_length=120,unique=True)
    Slug = models.CharField(max_length=120,unique=True,null=True,blank=True)
    Wine_With_Dienner = models.ManyToManyField(AwProducts,blank=True, related_name='AwProducts_with_dinner')
    Dinner_Image = models.ImageField(upload_to=user_directory_path,null=True,blank=True)
    Short_Description = models.TextField(null=True,blank=True)
    Description = models.TextField(null=True,blank=True)
    Status = models.BooleanField(default=True)
    Created_by = models.ForeignKey(User,  on_delete=models.SET_NULL, null=True, blank=True,related_name='AwDinner_Created_by')
    Created_date = models.DateTimeField(default=django.utils.timezone.now)
    Updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name='AwDinner_Updated_by')
    Updated_date = models.DateTimeField(default=django.utils.timezone.now)


    def get_absolute_url(self):
        return reverse('admin_manage_dinner:dinner')
    def __str__(self):
        return str(self.Dinner_Name)

    class Meta:
        verbose_name_plural = "AW Dinner"

def pre_save_create_slug(sender, instance, *args, **kwargs):
    if not instance.Slug:
        instance.Slug= slug_generator_for_AAwDinner(instance)
pre_save.connect(pre_save_create_slug, sender=AwDinner)