# Generated by Django 3.0.4 on 2020-04-28 10:29

import admin_manage_producer.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admin_manage_producer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AwProducers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Winnery_Name', models.CharField(max_length=120, unique=True)),
                ('Producer_Image', models.ImageField(upload_to=admin_manage_producer.models.user_directory_path)),
                ('Description', models.TextField(blank=True, null=True)),
                ('Status', models.BooleanField(default=True)),
                ('Created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='User_Created_by', to=settings.AUTH_USER_MODEL)),
                ('Set_To', models.ManyToManyField(blank=True, related_name='AwProducers_set_to', to='admin_manage_producer.AwSetTo')),
                ('Updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='User_Updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'AW Producers',
            },
        ),
    ]
