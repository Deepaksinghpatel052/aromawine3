from django.db import models
from django.contrib.auth.models import User
import django
from admin_manage_products.models import AwProducts,AwProductPrice
from addressbook_user.models import AwAddressBook
from manage_event.models import AwEvent
from wineproject.utils import  unique_id_generator_for_order
from django.db.models.signals import pre_save
from datetime import date

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







class AwOrders(models.Model):
    User = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='User_Order')
    order_id = models.CharField(max_length=120,unique=True,null=True, blank=True)
    Order_address = models.ForeignKey(AwAddressBook, on_delete=models.SET_NULL, null=True, blank=True, related_name='order_AwAddressBook')
    Order_Type = models.CharField(max_length=120,null=True, blank=True)
    Notes = models.TextField(null=True,blank=True)
    Quentity = models.IntegerField(default=0)
    Order_Product_Amount = models.FloatField(default=0)
    Order_Gst_Amount = models.FloatField(default=0)
    order_amount = models.IntegerField(default=0)
    Use_coupon = models.BooleanField(default=False)
    Cupon_Code = models.CharField(max_length=120,null=True, blank=True)
    Cupon_Discount = models.FloatField(default=0)
    Amount = models.IntegerField(default=0)
    Order_Status = models.BooleanField(default=False)
    order_place = models.BooleanField(default=False)
    Order_Status_Set = models.CharField(default='Active',max_length=120)
    Payment_Status = models.BooleanField(default=False)
    Payment_Method = models.CharField(max_length=120,null=True, blank=True)
    shipping_charge = models.IntegerField(default=0)
    shipping_Payment_Status = models.BooleanField(default=False)
    shipping_Payment_Method = models.CharField(max_length=120, null=True, blank=True)
    Order_Date = models.DateTimeField(default=django.utils.timezone.now)
    delivery_Date = models.DateTimeField(null=True, blank=True)
    Payment_Date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.order_id)

    class Meta:
        verbose_name_plural = "Aw Orders"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


def pre_save_create_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id= unique_id_generator_for_order(instance)
pre_save.connect(pre_save_create_order_id, sender=AwOrders)


def user_directory_path(instance, filename):
    producer_id_in_list = instance.Order_id.order_id.split(" ")
    today_date = date.today()
    producer_id_in_string = '_'.join([str(elem) for elem in producer_id_in_list])
    return '{0}/{1}'.format(producer_id_in_string+"/order_image/"+str(today_date.year)+"/"+str(today_date.month)+"/"+str(today_date.day),filename)



class AwOrderNote(models.Model):
    User = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='User_AwOrderNote')
    Order_id = models.ForeignKey(AwOrders, on_delete=models.SET_NULL, null=True, blank=True,related_name='orderId_AwOrderNote')
    Order_For = models.CharField(max_length=120,null=True, blank=True) #  # Like Cellar Delivered & Tickets
    Note = models.TextField(null=True,blank=True)
    Attachment = models.ImageField(upload_to=user_directory_path,null=True,blank=True)
    Display_Status = models.BooleanField(default=False)
    Date = models.DateTimeField(default=django.utils.timezone.now,blank=True,null=True)

    def __str__(self):
        return str(self.Note)

    class Meta:
        verbose_name_plural = "Aw Order Note"

class AwOrederItem(models.Model):
    User = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='User_OrderItem')
    Order_id = models.ForeignKey(AwOrders, on_delete=models.SET_NULL, null=True, blank=True, related_name='orderId_OrderItem')
    Product_Cellar = models.ForeignKey(AwProducts, on_delete=models.CASCADE, null=True, blank=True,related_name='AwProducts_AwOrederItem')
    Product_Delivered = models.ForeignKey(AwProducts, on_delete=models.CASCADE, null=True, blank=True,related_name='AwProducts_AwOrederItem_Delivered')
    Event_Ticket = models.ForeignKey(AwEvent, on_delete=models.CASCADE, null=True, blank=True,related_name='AwEvent_AwOrederItem')
    Year = models.CharField(max_length=120,null=True, blank=True,)
    Type = models.CharField(max_length=120,null=True, blank=True,)
    Case_Formate_text = models.CharField(max_length=120,null=True, blank=True)
    Case_Formate = models.ForeignKey(AwProductPrice, on_delete=models.SET_NULL, null=True, blank=True, related_name='Case_Formate_AwOrderitem')
    Cost_of_product = models.FloatField(default=0)
    Gst = models.FloatField(default=0)
    Duty = models.FloatField(default=0)
    Quentity = models.IntegerField(default=0)
    Total_cost = models.FloatField(default=0)

    def __str__(self):
        return str(self.Order_id)

    class Meta:
        verbose_name_plural = "Aw Order Items"


class AwAddToCard(models.Model):
    User = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='User_AwAddToCard')
    Cookies_id = models.CharField(max_length=120,null=True, blank=True)
    Order_Type = models.CharField(max_length=120,default='Cellar')    # Like Cellar Delivered & Tickets
    Product_Cellar = models.ForeignKey(AwProducts, on_delete=models.CASCADE, null=True, blank=True,related_name='AwProducts_AwAddToCard')
    Product_Delivered = models.ForeignKey(AwProducts, on_delete=models.CASCADE, null=True, blank=True,related_name='AwProducts_AwAddToCard_Delivered')
    order_item_id = models.ForeignKey(AwOrederItem, on_delete=models.CASCADE, null=True, blank=True,related_name='AwProducts_AwAddToCard_Delivered')
    Event_Ticket = models.ForeignKey(AwEvent, on_delete=models.CASCADE, null=True, blank=True,related_name='AwEvent_AwAddToCard')
    Year = models.CharField(max_length=120,null=True, blank=True,)
    Type = models.CharField(max_length=120,null=True, blank=True,)
    Old_Cost = models.FloatField(default=0)
    Case_Formate = models.ForeignKey(AwProductPrice, on_delete=models.SET_NULL, null=True, blank=True, related_name='Case_Formate_AwProductPrice')
    Quentity = models.IntegerField(default=0)
    Date = models.DateTimeField(default=django.utils.timezone.now)


    def __str__(self):
        return str(self.User)

    class Meta:
        verbose_name_plural = "Aw Add To Card"
