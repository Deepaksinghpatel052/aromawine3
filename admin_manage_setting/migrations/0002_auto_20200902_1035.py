# Generated by Django 3.0.6 on 2020-09-02 10:35

import admin_manage_setting.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_manage_setting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='awadminsetting',
            name='Logo',
            field=models.FileField(upload_to=admin_manage_setting.models.user_directory_path),
        ),
    ]