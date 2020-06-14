from django.db import models
import django
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from wineproject.utils import  slug_generator_for_color 
# Create your models here.

class AwColor(models.Model):
    Color_name = models.CharField(max_length=120,unique=True)
    Slug = models.CharField(max_length=120,null=True,blank=True)
    Description = models.TextField(null=True,blank=True)
    Status =models.BooleanField(default=True)
    Created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name='Created_by_AwColor')
    Created_date = models.DateTimeField(default=django.utils.timezone.now)
    Updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name='Updated_by_AwColor')
    Updated_date = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return str(self.Color_name)

    class Meta:
        verbose_name_plural = "AW Color"

def pre_save_create_slug(sender, instance, *args, **kwargs):
    if not instance.Slug:
        instance.Slug= slug_generator_for_color(instance)

pre_save.connect(pre_save_create_slug, sender=AwColor)