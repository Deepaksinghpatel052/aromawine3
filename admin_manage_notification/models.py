from django.db import models
import django
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class AwNotification(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name='AwNotification_User')
    Description = models.TextField(null=True,blank=True)
    Send_Status = models.BooleanField(default=False)
    Created_by =  models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name='AwNotification_Created_by')
    Created_date = models.DateTimeField(default=django.utils.timezone.now)
    Send_date = models.DateTimeField(null=True, blank=True)
    Read_Status = models.BooleanField(default=False)
    Read_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name_plural = "AW Notification"