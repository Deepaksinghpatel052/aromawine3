# Generated by Django 3.0.6 on 2020-08-01 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_manage_cupon_code', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='awcuponcode',
            name='Type',
            field=models.CharField(help_text='A for Amount & P for Percentage', max_length=120),
        ),
    ]