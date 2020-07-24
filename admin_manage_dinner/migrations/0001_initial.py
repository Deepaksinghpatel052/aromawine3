# Generated by Django 3.0.6 on 2020-07-22 07:55

import admin_manage_dinner.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admin_manage_products', '0005_auto_20200718_0526'),
    ]

    operations = [
        migrations.CreateModel(
            name='AwDinner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dinner_Name', models.CharField(max_length=120, unique=True)),
                ('Slug', models.CharField(blank=True, max_length=120, null=True, unique=True)),
                ('Dinner_Image', models.ImageField(upload_to=admin_manage_dinner.models.user_directory_path)),
                ('Short_Description', models.TextField(blank=True, null=True)),
                ('Description', models.TextField(blank=True, null=True)),
                ('Status', models.BooleanField(default=True)),
                ('Created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='AwDinner_Created_by', to=settings.AUTH_USER_MODEL)),
                ('Updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='AwDinner_Updated_by', to=settings.AUTH_USER_MODEL)),
                ('Wine_With_Dienner', models.ManyToManyField(blank=True, related_name='AwProducts_with_dinner', to='admin_manage_products.AwProducts')),
            ],
            options={
                'verbose_name_plural': 'AW Dinner',
            },
        ),
    ]
