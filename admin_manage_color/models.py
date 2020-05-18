from django.db import models
import django
from django.contrib.auth.models import User
# Create your models here.

class AwColor(models.Model):
    Color_name = models.CharField(max_length=120,unique=True)
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