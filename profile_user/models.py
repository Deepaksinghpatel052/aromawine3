from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class AwUserInfo(models.Model):
    User = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='User_AwUserInfo')
    Title  = models.CharField(max_length=120)
    Contact_no = models.IntegerField(default=0)


    def __str__(self):
        return str(self.User)

    class Meta:
        verbose_name_plural = "Aw User Infg"