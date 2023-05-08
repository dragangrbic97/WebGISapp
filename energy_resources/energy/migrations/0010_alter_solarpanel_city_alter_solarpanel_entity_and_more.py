# Generated by Django 4.1.7 on 2023-04-11 19:20

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energy', '0009_alter_solarpanel_document_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solarpanel',
            name='city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='solarpanel',
            name='entity',
            field=models.CharField(choices=[('RS', 'Republic of Srpska'), ('FBiH', 'Federation of Bosnia and Herzegovina'), ('BD', 'District Brcko')], max_length=50),
        ),
        migrations.AlterField(
            model_name='solarpanel',
            name='field_strength',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='solarpanel',
            name='geometry',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326),
        ),
        migrations.AlterField(
            model_name='windpowerplant',
            name='city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='windpowerplant',
            name='entity',
            field=models.CharField(choices=[('RS', 'Republic of Srpska'), ('FBiH', 'Federation of Bosnia and Herzegovina'), ('BD', 'District Brcko')], max_length=50),
        ),
        migrations.AlterField(
            model_name='windpowerplant',
            name='geometry',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326),
        ),
        migrations.AlterField(
            model_name='windpowerplant',
            name='power_supplied',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]