# Generated by Django 3.0.6 on 2020-12-24 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_manage_products', '0018_auto_20201221_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='awproducts',
            name='Product_name',
            field=models.CharField(max_length=120),
        ),
    ]