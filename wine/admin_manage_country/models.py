from django.db import models
from admin_manage_producer.models import AwSetTo
import django
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse
# Create your models here.



def user_directory_path(instance, filename):
    producer_id_in_list = instance.Country_Name.split(" ")
    today_date = date.today()
    producer_id_in_string = '_'.join([str(elem) for elem in producer_id_in_list])
    return '{0}/{1}'.format(producer_id_in_string+"/country/"+str(today_date.year)+"/"+str(today_date.month)+"/"+str(today_date.day),filename)


class AwCountry(models.Model):
    Country_Name = models.CharField(max_length=120, unique=True)
    Set_To = models.ManyToManyField(AwSetTo, blank=True, related_name='AwCountry_set_to')
    Country_Image = models.ImageField(upload_to=user_directory_path)
    Description = models.TextField(null=True, blank=True)
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