# Generated by Django 3.0.4 on 2020-04-29 13:58

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admin_manage_categoryes', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AwCategoryes',
            new_name='AwCategory',
        ),
        migrations.RenameField(
            model_name='awcategory',
            old_name='Categorye_name',
            new_name='Category_name',
        ),
    ]
