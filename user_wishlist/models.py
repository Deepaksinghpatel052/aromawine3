from django.db import models
from django.contrib.auth.models import User
import django
from admin_manage_products.models import AwProducts
from orders.models import AwProductPrice
# Create your models here.

class AwWishList(models.Model):
    user_info = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name='AwWishList_Created_by')
    Product = models.ForeignKey(AwProducts, on_delete=models.CASCADE, null=True, blank=True,related_name='AwWishList_Product')
    Case_Formate = models.ForeignKey(AwProductPrice, on_delete=models.SET_NULL, null=True, blank=True,related_name='Case_Formate_AwWishList')
    Created_date = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return str(self.Product)

    class Meta:
        verbose_name_plural = "Aw WishList"