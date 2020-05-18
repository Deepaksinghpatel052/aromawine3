from django.db import models
import django
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class AwClassification(models.Model):
    Classification_Name = models.CharField(max_length=120,unique=True)
    Status = models.BooleanField(default=True)
    Created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='AwClassification_Created_by')
    Created_date = models.DateTimeField(default=django.utils.timezone.now)
    Updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name='AwClassification_Updated_by')
    Updated_date = models.DateTimeField(default=django.utils.timezone.now)


    def __str__(self):
        return str(self.Classification_Name)
    class Meta:
        verbose_name_plural = "Aw Classification"

    def get_absolute_url(self):
        return reverse('admin_manage_classification:classification')