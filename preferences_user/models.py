from django.db import models
from django.contrib.auth.models import User
import django
from admin_manage_perferences.models import Service_Interests
from admin_manage_categoryes.models import AwCategory
# Create your models here.


class User_Service_Interests(models.Model):
    Service_interests_by_user = models.CharField(max_length=120)
    Interested_User = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name='service_interests_user')
    Service_interest = models.ForeignKey(Service_Interests, on_delete=models.SET_NULL, null=True, blank=True,related_name='service_interests_name')
    Date = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return str(self.Service_interests_by_user)

    class Meta:
        verbose_name_plural = "Aw User Service Interests"


