from django.db import models
import django
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class AwMembership(models.Model):
    Membership_name = models.CharField(max_length=120,unique=True)
    min_price = models.IntegerField(default=0)
    max_price = models.IntegerField(default=0)
    Created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='Awmembershilp_Created_by')
    Created_date = models.DateTimeField(default=django.utils.timezone.now)


    def __str__(self):
        return str(self.Membership_name)
    class Meta:
        verbose_name_plural = "AW Membership"