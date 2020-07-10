from django.db import models
from django.contrib.auth.models import User
import django
from admin_manage_products.models import AwProducts,AwProductPrice
from addressbook_user.models import AwAddressBook
from wineproject.utils import  unique_id_generator_for_order
from django.db.models.signals import pre_save

# Create your models here.

# class AwOrders(models.Model):
#     User = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name='User_Orders')
#     Product = models.ForeignKey(AwProducts, on_delete=models.SET_NULL, null=True, blank=True,related_name='Product_Orders')
#     Type = models.CharField(max_length=120)
#     Quentity = models.IntegerField(default=0)
#     Order_date = models.DateTimeField(default=django.utils.timezone.now)
#     # def get_absolute_url(self):
#     #     return reverse('admin_manage_products:products')
#     def __str__(self):
#         return str(self.Product)
#
#     class Meta:
#         verbose_name_plural = "Aw Orders"

class AwAddToCard(models.Model):
    User = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='User_AwAddToCard')
    Product = models.ForeignKey(AwProducts, on_delete=models.CASCADE, null=True, blank=True,related_name='AwProducts_AwAddToCard')
    Year = models.CharField(max_length=120)
    Type = models.CharField(max_length=120)
    Case_Formate = models.ForeignKey(AwProductPrice, on_delete=models.SET_NULL, null=True, blank=True, related_name='Case_Formate_AwProductPrice')
    Quentity = models.IntegerField(default=0)
    Date = models.DateTimeField(default=django.utils.timezone.now)


    def __str__(self):
        return str(self.User)

    class Meta:
        verbose_name_plural = "Aw Add To Card"

class AwOrders(models.Model):
    User = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='User_Order')
    order_id = models.CharField(max_length=120,unique=True,null=True, blank=True)
    Order_address = models.ForeignKey(AwAddressBook, on_delete=models.SET_NULL, null=True, blank=True, related_name='order_AwAddressBook')
    Order_Type = models.CharField(max_length=120,null=True, blank=True)
    Notes = models.TextField(null=True,blank=True)
    Quentity = models.IntegerField(default=0)
    Amount = models.IntegerField(default=0)
    Payment_Status = models.BooleanField(default=True)
    Payment_Method = models.CharField(max_length=120,null=True, blank=True)
    Order_Date = models.DateTimeField(default=django.utils.timezone.now)
    delivery_Date = models.DateTimeField(null=True, blank=True)
    Payment_Date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.order_id)

    class Meta:
        verbose_name_plural = "Aw Orders"


def pre_save_create_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id= unique_id_generator(instance)
pre_save.connect(pre_save_create_order_id, sender=AwOrders)
