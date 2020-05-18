from django.db import models
import django
from datetime import date
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class AwSetTo(models.Model):
    Title = models.CharField(max_length=50)
    Status = models.BooleanField(default=True)
    Created_date = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return str(self.Title)
    class Meta:
        verbose_name_plural = "AW Set To"


def user_directory_path(instance, filename):
    producer_id_in_list = instance.Winnery_Name.split(" ")
    today_date = date.today()
    producer_id_in_string = '_'.join([str(elem) for elem in producer_id_in_list])
    return '{0}/{1}'.format(producer_id_in_string+"/producer/"+str(today_date.year)+"/"+str(today_date.month)+"/"+str(today_date.day),filename)


class AwProducers(models.Model):
    Winnery_Name = models.CharField(max_length=120,unique=True)
    Set_To = models.ManyToManyField(AwSetTo,blank=True, related_name='AwProducers_set_to')
    Producer_Image = models.ImageField(upload_to=user_directory_path)
    Description = models.TextField(null=True,blank=True)
    Status = models.BooleanField(default=True)
    Created_by = models.ForeignKey(User,  on_delete=models.SET_NULL, null=True, blank=True,related_name='User_Created_by')
    Created_date = models.DateTimeField(default=django.utils.timezone.now)
    Updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name='User_Updated_by')
    Updated_date = models.DateTimeField(default=django.utils.timezone.now)


    def get_absolute_url(self):
        return reverse('admin_manage_producer:producer')
    def __str__(self):
        return str(self.Winnery_Name)

    class Meta:
        verbose_name_plural = "AW Producers"

