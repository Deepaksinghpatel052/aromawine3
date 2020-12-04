# Generated by Django 3.0.6 on 2020-11-17 06:32

import admin_manage_special_offers.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AwSpecialOffers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=120, unique=True)),
                ('Priority_set', models.IntegerField(default=0, unique=True)),
                ('Description', models.TextField(blank=True, null=True)),
                ('Banner_Image', models.ImageField(upload_to=admin_manage_special_offers.models.user_directory_path)),
                ('Link', models.URLField()),
                ('Created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='AwSpecialOffers_Created_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Aw Special Offers',
            },
        ),
    ]
