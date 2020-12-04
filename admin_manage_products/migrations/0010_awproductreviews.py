# Generated by Django 3.0.6 on 2020-11-19 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_manage_products', '0009_auto_20201119_1850'),
    ]

    operations = [
        migrations.CreateModel(
            name='AwProductReviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LWineCode', models.CharField(blank=True, max_length=120, null=True)),
                ('Publication', models.CharField(blank=True, max_length=120, null=True)),
                ('reviewer', models.CharField(blank=True, max_length=120, null=True)),
                ('reviewDate', models.CharField(blank=True, max_length=120, null=True)),
                ('scoreRaw', models.CharField(blank=True, max_length=120, null=True)),
                ('scoreFrom', models.CharField(blank=True, max_length=120, null=True)),
                ('scoreTo', models.CharField(blank=True, max_length=120, null=True)),
                ('scoreMedian', models.CharField(blank=True, max_length=120, null=True)),
                ('drinkFrom', models.CharField(blank=True, max_length=120, null=True)),
                ('tastingNote', models.CharField(blank=True, max_length=120, null=True)),
                ('externalReference', models.CharField(blank=True, max_length=120, null=True)),
                ('externalLink', models.CharField(blank=True, max_length=120, null=True)),
                ('externalId', models.CharField(blank=True, max_length=120, null=True)),
            ],
            options={
                'verbose_name_plural': 'Aw Product Reviews',
            },
        ),
    ]
