from django.db import models
from django.contrib.auth.models import User
from django_date_extensions.fields import ApproximateDateField
import django
# Create your models here.



class AwPaymentMethod(models.Model):
    Name_on_Card=models.CharField(max_length=120)
    Card_Number=models.BigIntegerField(unique=True)
    Expiry_Date= models.DateField()
    CVC_CVV=models.IntegerField()
    ZIP=models.IntegerField()
    Paypal=models.BooleanField(default=False)
    Pay_on_delivery=models.BooleanField(default=False)
    active_status=models.BooleanField(default=True)
    Created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name='Created_by_AwPaymentMethod')
    Created_date = models.DateTimeField(default=django.utils.timezone.now)


    def __str__(self):
        return str(self.Name_on_Card)

    class Meta:
        verbose_name_plural = "AW Payment Method"
