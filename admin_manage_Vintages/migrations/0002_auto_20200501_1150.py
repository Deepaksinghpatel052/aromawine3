# Generated by Django 3.0.4 on 2020-05-01 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_manage_Vintages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='awvintages',
            name='Vintages_Name',
        ),
        migrations.AddField(
            model_name='awvintages',
            name='Vintages_Year',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]
