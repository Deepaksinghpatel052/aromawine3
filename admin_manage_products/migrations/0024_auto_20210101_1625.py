# Generated by Django 3.0.6 on 2021-01-01 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_manage_size', '0001_initial'),
        ('admin_manage_products', '0023_auto_20201231_1614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='awproducts',
            name='Bottel_Size',
        ),
        migrations.AddField(
            model_name='awproducts',
            name='Bottel_Size',
            field=models.ManyToManyField(related_name='AwSize_Bottel_Size', to='admin_manage_size.AwSize'),
        ),
    ]