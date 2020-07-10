from django.db import models
import django
from wineproject.utils import  slug_generator_for_AwCmsPaage
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from datetime import datetime
from datetime import date
# Create your models here.
class AwAboutAromaWines(models.Model):
    Title = models.CharField(max_length=120)
    description = models.TextField()
    Create_date = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return str(self.Title)
    class Meta:
        verbose_name_plural = "Aw About Aroma Wines"

def user_directory_path(instance, filename):
    producer_id_in_list = instance.Title.split(" ")
    today_date = date.today()
    producer_id_in_string = '_'.join([str(elem) for elem in producer_id_in_list])
    return '{0}/{1}'.format("cms_page/"+producer_id_in_string+"/"+str(today_date.year)+"/"+str(today_date.month)+"/"+str(today_date.day),filename)


class AwCmsPaage(models.Model):
    Title = models.CharField(max_length=120,unique=True)
    Slug = models.CharField(max_length=120,null=True,blank=True)
    Background_Image = models.ImageField(upload_to=user_directory_path)
    description = models.TextField()
    Create_date = models.DateTimeField(default=django.utils.timezone.now)
    Created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='User_AwCmsPaage_Created_by')
    Updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='User_AwCmsPaage_Updated_by')

    def __str__(self):
        return str(self.Title)
    class Meta:
        verbose_name_plural = "Aw Cms Paage"

def pre_save_create_slug(sender, instance, *args, **kwargs):
    if not instance.Slug:
        instance.Slug= slug_generator_for_AwCmsPaage(instance)
pre_save.connect(pre_save_create_slug, sender=AwCmsPaage)