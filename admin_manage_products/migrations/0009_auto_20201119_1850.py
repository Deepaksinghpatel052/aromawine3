# Generated by Django 3.0.6 on 2020-11-19 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_manage_products', '0008_awproducts_lwine'),
    ]

    operations = [
        migrations.RenameField(
            model_name='awproducts',
            old_name='LWine',
            new_name='LWineCode',
        ),
    ]