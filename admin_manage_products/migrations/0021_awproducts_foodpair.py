# Generated by Django 3.0.6 on 2020-12-30 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_manage_food_pair', '0001_initial'),
        ('admin_manage_products', '0020_auto_20201229_2216'),
    ]

    operations = [
        migrations.AddField(
            model_name='awproducts',
            name='FoodPair',
            field=models.ManyToManyField(blank=True, null=True, related_name='AwWine_AwFoodpair', to='admin_manage_food_pair.AwFoodpair'),
        ),
    ]