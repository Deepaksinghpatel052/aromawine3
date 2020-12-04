from django.db import models
import django
from django.contrib.auth.models import User
# Create your models here.

def user_directory_path_for_product(instance, filename):
    producer_id_in_list = instance.Category_name.split(" ")
    today_date = date.today()
    producer_id_in_string = '_'.join([str(elem) for elem in producer_id_in_list])
    return '{0}/{1}'.format("AwWinePalate/"+producer_id_in_string+"/"+str(today_date.year)+"/"+str(today_date.month)+"/"+str(today_date.day),filename)



class AwWinePalateCategories(models.Model):
    Category_name = models.CharField(max_length=120,unique=True,null=True, blank=True)
    Category_Color = models.CharField(max_length=120,null=True, blank=True)
    Category_Type = models.CharField(max_length=120,null=True, blank=True)
    Category_image = models.ImageField(upload_to=user_directory_path_for_product, null=True, blank=True)
    Created_date = models.DateTimeField(default=django.utils.timezone.now)

    def __str__(self):
        return str(self.Category_name)

    class Meta:
        verbose_name_plural = "Aw Wine Palate Categories"

class AwWinePalateFlavors(models.Model):
    Category = models.ForeignKey(AwWinePalateCategories, on_delete=models.SET_NULL, null=True, blank=True,related_name='Category_AwWinePalateCategories')
    Type = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return str(self.Type)

    class Meta:
        verbose_name_plural = "Aw Wine Palate Flavors"


class AwUserPalateWine(models.Model):
    User = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='User_Palates')
    Category_name = models.CharField(max_length=120,  null=True, blank=True)
    Type = models.CharField(max_length=120, null=True, blank=True)
    CategoryNameAndType = models.CharField(max_length=120, null=True, blank=True)
    Created_date = models.DateTimeField(default=django.utils.timezone.now)


    def __str__(self):
        return str(self.Type)

    class Meta:
        verbose_name_plural = "Aw User Palate Wine"
