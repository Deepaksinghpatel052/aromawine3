from django.db import models
from django.contrib.auth.models import User
import django
from django.urls import reverse
from admin_manage_producer.models import AwProducers
from admin_manage_categoryes.models import AwCategory
from admin_manage_color.models import AwColor
from admin_manage_appellation.models import AwAppellation
from admin_manage_size.models import AwSize
from admin_manage_classification.models import AwClassification
from admin_manage_Vintages.models import AwVintages
from admin_manage_varietals.models import AwVarietals
from admin_manage_country.models import AwCountry
from admin_manage_region.models import AwRegion
from admin_manage_grape.models import AwGrape
from django.db.models.signals import pre_save
from wineproject.utils import  unique_id_generator , slug_generator_for_product
from datetime import date
# Create your models here.

class AwWineType(models.Model):
    Type = models.CharField(max_length=120,unique=True)
    Status = models.BooleanField(default=True)
    Created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name='AwWineType_Created_by')
    Created_date = models.DateTimeField(default=django.utils.timezone.now)
    Updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name='AwWineType_Updated_by')
    Updated_date = models.DateTimeField(default=django.utils.timezone.now)

    def get_absolute_url(self):
        return reverse('admin_manage_products:products')
    def __str__(self):
        return str(self.Type)

    class Meta:
        verbose_name_plural = "Aw Wine Type"


class AwProducts(models.Model):
    Product_id = models.CharField(max_length=120,unique=True)
    Select_Type = models.ForeignKey(AwWineType, on_delete=models.SET_NULL, null=True, blank=True,related_name='AwProducts_Created_by')
    Product_name  = models.CharField(max_length=120,unique=True)
    Product_slug  = models.CharField(max_length=120,unique=True)
    Producer = models.ForeignKey(AwProducers, on_delete=models.SET_NULL, null=True, blank=True,related_name='AwProducts_Producer')
    Category = models.ManyToManyField(AwCategory, related_name='AwProducts_Category')
    Color = models.ForeignKey(AwColor, on_delete=models.SET_NULL,null=True, blank=True,  related_name='AwProducts_Color')
    Appellation = models.ManyToManyField(AwAppellation, related_name='AwProducts_Appellation')
    Bottel_Size = models.ForeignKey(AwSize, on_delete=models.SET_NULL,null=True, blank=True, related_name='AwProducts_Bottel_Size')
    Classification = models.ManyToManyField(AwClassification,  related_name='AwProducts_Classification')
    Vintage = models.ManyToManyField(AwVintages, related_name='AwProducts_Vintage')
    Varietals = models.ManyToManyField(AwVarietals, related_name='AwProducts_Varietals')
    Country = models.ForeignKey(AwCountry, on_delete=models.SET_NULL, null=True, blank=True,related_name='AwProducts_Country')
    Regions = models.ForeignKey(AwRegion, on_delete=models.SET_NULL, null=True, blank=True,related_name='AwProducts_Regions')
    Grape = models.ManyToManyField(AwGrape,  related_name='AwProducts_Grape')
    Status = models.BooleanField(default=True)
    Description = models.TextField(null=True,blank=True)
    Meta_Title = models.CharField(max_length=120,null=True,blank=True)
    Meta_Keyword = models.CharField(max_length=120,null=True,blank=True)
    Meta_Description = models.TextField(null=True,blank=True)
    Created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name='AwProducts_Created_by')
    Created_date = models.DateTimeField(default=django.utils.timezone.now)
    Updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name='AwProducts_Updated_by')
    Updated_date = models.DateTimeField(default=django.utils.timezone.now)


    # def get_absolute_url(self):
    #     return reverse('admin_manage_products:products')
    def __str__(self):
        return str(self.Product_name)

    class Meta:
        verbose_name_plural = "Aw Products"

def pre_save_create_product_id(sender, instance, *args, **kwargs):
    if not instance.Product_id:
        instance.Product_id= unique_id_generator(instance)


def pre_save_create_slug(sender, instance, *args, **kwargs):
    if not instance.Product_slug:
        instance.Product_slug= slug_generator_for_product(instance)

pre_save.connect(pre_save_create_product_id, sender=AwProducts)
pre_save.connect(pre_save_create_slug, sender=AwProducts)



def user_directory_path(instance, filename):
    producer_id_in_list = instance.Product.Product_name.split(" ")
    today_date = date.today()
    producer_id_in_string = '_'.join([str(elem) for elem in producer_id_in_list])
    return '{0}/{1}'.format(producer_id_in_string+"/product_image/"+str(today_date.year)+"/"+str(today_date.month)+"/"+str(today_date.day),filename)


class AwProductImage(models.Model):
    Product = models.ForeignKey(AwProducts, on_delete=models.CASCADE, null=True, blank=True,related_name='AwProductImage_Product')
    Image_Type = models.CharField(max_length=120,null=True,blank=True)
    Image = models.ImageField(upload_to=user_directory_path)
    Status = models.BooleanField(default=True)
    Created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name='AwProductImage_Created_by')
    Created_date = models.DateTimeField(default=django.utils.timezone.now)
    Updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name='AwProductImage_Updated_by')
    Updated_date = models.DateTimeField(default=django.utils.timezone.now)

    # def get_absolute_url(self):
    #     return reverse('admin_manage_products:products')
    def __str__(self):
        return str(self.Image)

    class Meta:
        verbose_name_plural = "Aw Product Image"

class AwProductPrice(models.Model):
    Product = models.ForeignKey(AwProducts, on_delete=models.CASCADE, null=True, blank=True,related_name='AwProductPrice_Product')
    Vintage_Year = models.ForeignKey(AwVintages, on_delete=models.SET_NULL, null=True, blank=True,related_name='AwProductPrice_Vintage_Year')
    Bottle = models.CharField(max_length=120,null=True,blank=True)
    Retail_Cost = models.FloatField(default=0)
    Retail_Stock = models.IntegerField(default=0)
    Descount_Cost = models.FloatField(default=0)
    Duty = models.FloatField(default=0)
    GST = models.FloatField(default=0)
    Bond_Cost = models.FloatField(default=0)
    Bond_Stock = models.IntegerField(default=0)
    Bond_Descount_Cost = models.FloatField(default=0)
    Other_info = models.TextField(null=True,blank=True)
    Created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name='AwProductPrice_Created_by')
    Created_date = models.DateTimeField(default=django.utils.timezone.now)
    Updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name='AwProductPrice_Updated_by')
    Updated_date = models.DateTimeField(default=django.utils.timezone.now)

    # def get_absolute_url(self):
    #     return reverse('admin_manage_products:products')
    def __str__(self):
        return str(self.Vintage_Year)

    class Meta:
        verbose_name_plural = "Aw Product Price & Stock"