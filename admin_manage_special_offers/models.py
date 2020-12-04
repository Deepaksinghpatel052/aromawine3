from django.db import models
from django.contrib.auth.models import User
from datetime import date
import django
from django.urls import reverse
# Create your models here.

def user_directory_path(instance, filename):
    producer_id_in_list = instance.Title.split(" ")
    today_date = date.today()
    producer_id_in_string = '_'.join([str(elem) for elem in producer_id_in_list])
    return '{0}/{1}'.format("special_offer/"+producer_id_in_string+"/"+str(today_date.year)+"/"+str(today_date.month)+"/"+str(today_date.day),filename)




class AwSpecialOffers(models.Model):
    Title = models.CharField(max_length=120,unique=True)
    Priority_set = models.IntegerField(unique=True,default=0)
    Description = models.TextField(null=True,blank=True)
    Banner_Image = models.ImageField(upload_to=user_directory_path)
    Link = models.URLField(max_length=200)
    Created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name='AwSpecialOffers_Created_by')
    Created_date = models.DateTimeField(default=django.utils.timezone.now)


    def __str__(self):
        return str(self.Title)
    class Meta:
        verbose_name_plural = "Aw Special Offers"

    def get_absolute_url(self):
        return reverse('admin_manage_special_offers:special_offer')


