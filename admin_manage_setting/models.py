from django.db import models
from django.contrib.auth.models import User
import django
from datetime import date
from admin_manage_country.models import AwCountryUser
# Create your models here.

def user_directory_path(instance, filename):
    producer_id_in_list = instance.Project_Name.split(" ")
    today_date = date.today()
    producer_id_in_string = '_'.join([str(elem) for elem in producer_id_in_list])
    return '{0}/{1}'.format('project_logo/'+producer_id_in_string+"/"+str(today_date.year)+"/"+str(today_date.month)+"/"+str(today_date.day),filename)


def user_favicon_directory_path(instance, filename):
    producer_id_in_list = instance.Project_Name.split(" ")
    today_date = date.today()
    producer_id_in_string = '_'.join([str(elem) for elem in producer_id_in_list])
    return '{0}/{1}'.format("project_favicon/"+producer_id_in_string+"/"+str(today_date.year)+"/"+str(today_date.month)+"/"+str(today_date.day),filename)



class AwAllCountry(models.Model):
    Country_Name = models.CharField(max_length=120, unique=True)


    def __str__(self):
        return str(self.Country_Name)

    class Meta:
        verbose_name_plural = "Aw All Country"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)




class AwAdminSetting(models.Model):
    Project_Name = models.CharField(max_length=120, unique=True)
    Project_Tag_Line = models.CharField(max_length=120, unique=True)
    Logo = models.FileField(upload_to=user_directory_path)
    favicon = models.ImageField(upload_to=user_favicon_directory_path)
    Duty = models.FloatField(default=0)
    GST = models.FloatField(default=0)
    Analytics = models.TextField(null=True,blank=True)
    Manage_Delivery_Countries = models.ManyToManyField(AwAllCountry, related_name='AwAdminSetting_Vintage')
    Facebook = models.URLField(max_length=200,null=True,blank=True)
    Twitter = models.URLField(max_length=200,null=True,blank=True)
    Linkedin = models.URLField(max_length=200,null=True,blank=True)
    Instgram = models.URLField(max_length=200,null=True,blank=True)
    Google = models.URLField(max_length=200,null=True,blank=True)
    Yelp = models.URLField(max_length=200,null=True,blank=True)
    EMAIL_HOST = models.CharField(max_length=120, unique=True)
    EMAIL_USE_TLS  = models.BooleanField(default=True)
    EMAIL_PORT   = models.IntegerField(default=0)
    EMAIL_HOST_USER = models.EmailField(max_length=254)
    EMAIL_HOST_PASSWORD  = models.CharField(max_length=120, unique=True)



    def __str__(self):
        return str(self.Project_Name)

    class Meta:
        verbose_name_plural = "Aw Admin Setting"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)




class AwManageShipping(models.Model):
    Country = models.ForeignKey(AwCountryUser, on_delete=models.SET_NULL, null=True, blank=True,related_name='AwManageShipping_Country',unique=True)
    min_ordr_amount = models.FloatField(default=0)
    Shiping_Fees_min_order_amount = models.FloatField(default=0)
    Create_date = models.DateTimeField(default=django.utils.timezone.now)
    Created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name='AwManageShipping_Created_by')



    def __str__(self):
        return str(self.Country)

    class Meta:
        verbose_name_plural = "Aw Manage Shipping"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
