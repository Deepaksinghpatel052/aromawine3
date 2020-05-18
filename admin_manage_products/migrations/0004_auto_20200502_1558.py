# Generated by Django 3.0.4 on 2020-05-02 10:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('admin_manage_Vintages', '0002_auto_20200501_1150'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admin_manage_products', '0003_awproductimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='awproducts',
            name='Description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='awproductimage',
            name='Product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='AwProductImage_Product', to='admin_manage_products.AwProducts'),
        ),
        migrations.CreateModel(
            name='AwProductPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bottle', models.CharField(blank=True, max_length=120, null=True)),
                ('Retail_Cost', models.FloatField(default=0)),
                ('Retail_Stock', models.FloatField(default=0)),
                ('Descount_Cose', models.FloatField(default=0)),
                ('Duty', models.FloatField(default=0)),
                ('GST', models.FloatField(default=0)),
                ('Bond_Cost', models.FloatField(default=0)),
                ('Bond_Stock', models.FloatField(default=0)),
                ('Other_info', models.TextField(blank=True, null=True)),
                ('Created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='AwProductPrice_Created_by', to=settings.AUTH_USER_MODEL)),
                ('Product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='AwProductPrice_Product', to='admin_manage_products.AwProducts')),
                ('Updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='AwProductPrice_Updated_by', to=settings.AUTH_USER_MODEL)),
                ('Vintage_Year', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='AwProductPrice_Vintage_Year', to='admin_manage_Vintages.AwVintages')),
            ],
            options={
                'verbose_name_plural': 'Aw Product Price & Stock',
            },
        ),
    ]
