# Generated by Django 3.0.6 on 2020-07-24 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20200716_0828'),
    ]

    operations = [
        migrations.AddField(
            model_name='aworders',
            name='Cupon',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='aworders',
            name='Cupon_Discount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='aworders',
            name='order_amount',
            field=models.IntegerField(default=0),
        ),
    ]
