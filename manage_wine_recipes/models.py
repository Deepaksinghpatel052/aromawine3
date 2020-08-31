from django.db import models
from datetime import date
import django
from autoslug import AutoSlugField
from admin_manage_products.models import AwProducts
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
def user_directory_path(instance, filename):
    producer_id_in_list = instance.Name.split(" ")
    today_date = date.today()
    producer_id_in_string = '_'.join([str(elem) for elem in producer_id_in_list])
    return '{0}/{1}'.format(producer_id_in_string+"/wine_recipes/"+str(today_date.year)+"/"+str(today_date.month)+"/"+str(today_date.day),filename)




class AwWineRecipes(models.Model):
    Name  = models.CharField(max_length=120,unique=True)
    Slug = AutoSlugField(populate_from='Name', always_update=True,unique_with='Created_date__month',null=True, blank=True)
    Image = models.ImageField(upload_to=user_directory_path)
    Wine_With_Recipes = models.ManyToManyField(AwProducts, related_name='AwWineRecipes_Wine_With_Recipes')
    Short_Description = models.TextField(null=True, blank=True)
    Description = models.TextField(null=True, blank=True)
    Status = models.BooleanField(default=True)
    Created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name='AwWineRecipes_Created_by')
    Created_date = models.DateTimeField(default=django.utils.timezone.now)
    Updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name='AwWineRecipes_Updated_by')
    Updated_date = models.DateTimeField(default=django.utils.timezone.now)

    #     return reverse('admin_manage_products:products')
    def __str__(self):
        return str(self.Name)

    class Meta:
        verbose_name_plural = "Aw Wine Recipes"


    def get_absolute_url(self):
        return reverse('manage_wine_recipes:recipes')
