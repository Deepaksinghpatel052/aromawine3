# Generated by Django 3.0.4 on 2020-05-02 09:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('admin_manage_classification', '0001_initial'),
        ('admin_manage_producer', '0002_awproducers'),
        ('admin_manage_size', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admin_manage_grape', '0001_initial'),
        ('admin_manage_country', '0001_initial'),
        ('admin_manage_Vintages', '0002_auto_20200501_1150'),
        ('admin_manage_varietals', '0001_initial'),
        ('admin_manage_color', '0002_auto_20200502_1431'),
        ('admin_manage_categoryes', '0002_auto_20200429_1928'),
        ('admin_manage_appellation', '0001_initial'),
        ('admin_manage_region', '0001_initial'),
        ('admin_manage_products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AwProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_id', models.CharField(max_length=120, unique=True)),
                ('Product_name', models.CharField(max_length=120, unique=True)),
                ('Product_slug', models.CharField(max_length=120, unique=True)),
                ('Status', models.BooleanField(default=True)),
                ('Meta_Title', models.CharField(blank=True, max_length=120, null=True)),
                ('Meta_Keyword', models.CharField(blank=True, max_length=120, null=True)),
                ('Meta_Description', models.TextField(blank=True, null=True)),
                ('Created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Appellation', models.ManyToManyField(blank=True, null=True, related_name='AwProducts_Appellation', to='admin_manage_appellation.AwAppellation')),
                ('Bottel_Size', models.ManyToManyField(blank=True, null=True, related_name='AwProducts_Bottel_Size', to='admin_manage_size.AwSize')),
                ('Category', models.ManyToManyField(blank=True, null=True, related_name='AwProducts_Category', to='admin_manage_categoryes.AwCategory')),
                ('Classification', models.ManyToManyField(blank=True, null=True, related_name='AwProducts_Classification', to='admin_manage_classification.AwClassification')),
                ('Color', models.ManyToManyField(blank=True, null=True, related_name='AwProducts_Color', to='admin_manage_color.AwColor')),
                ('Country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='AwProducts_Country', to='admin_manage_country.AwCountry')),
                ('Created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='AwProducts_Created_by', to=settings.AUTH_USER_MODEL)),
                ('Grape', models.ManyToManyField(blank=True, null=True, related_name='AwProducts_Grape', to='admin_manage_grape.AwGrape')),
                ('Producer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='AwProducts_Producer', to='admin_manage_producer.AwProducers')),
                ('Regions', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='AwProducts_Regions', to='admin_manage_region.AwRegion')),
                ('Select_Type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='AwProducts_Created_by', to='admin_manage_products.AwWineType')),
                ('Updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='AwProducts_Updated_by', to=settings.AUTH_USER_MODEL)),
                ('Varietals', models.ManyToManyField(blank=True, null=True, related_name='AwProducts_Varietals', to='admin_manage_varietals.AwVarietals')),
                ('Vintage', models.ManyToManyField(blank=True, null=True, related_name='AwProducts_Vintage', to='admin_manage_Vintages.AwVintages')),
            ],
            options={
                'verbose_name_plural': 'Aw Products',
            },
        ),
    ]
