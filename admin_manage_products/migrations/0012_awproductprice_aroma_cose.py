# Generated by Django 3.0.6 on 2020-12-14 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_manage_products', '0011_awproductreviews_drinkto'),
    ]

    operations = [
        migrations.AddField(
            model_name='awproductprice',
            name='Aroma_Cose',
            field=models.FloatField(default=0),
        ),
    ]