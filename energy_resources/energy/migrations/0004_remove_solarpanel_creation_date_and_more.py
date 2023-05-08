# Generated by Django 4.1.7 on 2023-03-29 17:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energy', '0003_alter_solarpanel_canton_alter_solarpanel_zone_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solarpanel',
            name='creation_date',
        ),
        migrations.RemoveField(
            model_name='solarpanel',
            name='last_user',
        ),
        migrations.RemoveField(
            model_name='solarpanel',
            name='modification_date',
        ),
        migrations.RemoveField(
            model_name='windpowerplant',
            name='creation_date',
        ),
        migrations.RemoveField(
            model_name='windpowerplant',
            name='last_user',
        ),
        migrations.RemoveField(
            model_name='windpowerplant',
            name='modification_date',
        ),
        migrations.AlterField(
            model_name='solarpanel',
            name='altitude',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='solarpanel',
            name='canton',
            field=models.CharField(blank=True, choices=[("('USK', 'Unsko-sanski')", 'Usk'), ("('POS', 'Posavski')", 'Pos'), ("('TUZ', 'Tuzlanski')", 'Tuz'), ("('ZDK', 'Zeničko-dobojski')", 'Zdk'), ("('BPO', 'Bosansko-podrinjski')", 'Bpo'), ("('SBK', 'Srednjobosanski')", 'Sbk'), ("('HN', 'Hercegovačko-neretvanski')", 'Hn'), ('HB', 'Hercegbosanski')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='solarpanel',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='solarpaneldocuments/', validators=[django.core.validators.FileExtensionValidator(['pdf'])]),
        ),
        migrations.AlterField(
            model_name='solarpanel',
            name='entity',
            field=models.CharField(choices=[("('RS', 'Republika Srpska')", 'Rs'), ("('FBiH', 'Federacija Bosne i Hercegovine')", 'Fbih'), ('BD', 'Brčko distrikt')], max_length=50),
        ),
        migrations.AlterField(
            model_name='solarpanel',
            name='manufacturer',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='solarpanel',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='solarpanel',
            name='owner_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='solarpanel',
            name='panel_angle',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='solarpanel',
            name='zone',
            field=models.CharField(blank=True, choices=[("('U', 'Urban')", 'U'), ('R', 'Rural')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='windpowerplant',
            name='altitude',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='windpowerplant',
            name='canton',
            field=models.CharField(blank=True, choices=[("('USK', 'Unsko-sanski')", 'Usk'), ("('POS', 'Posavski')", 'Pos'), ("('TUZ', 'Tuzlanski')", 'Tuz'), ("('ZDK', 'Zeničko-dobojski')", 'Zdk'), ("('BPO', 'Bosansko-podrinjski')", 'Bpo'), ("('SBK', 'Srednjobosanski')", 'Sbk'), ("('HN', 'Hercegovačko-neretvanski')", 'Hn'), ('HB', 'Hercegbosanski')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='windpowerplant',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='windpowerplantdocuments/', validators=[django.core.validators.FileExtensionValidator(['pdf'])]),
        ),
        migrations.AlterField(
            model_name='windpowerplant',
            name='entity',
            field=models.CharField(choices=[("('RS', 'Republika Srpska')", 'Rs'), ("('FBiH', 'Federacija Bosne i Hercegovine')", 'Fbih'), ('BD', 'Brčko distrikt')], max_length=50),
        ),
        migrations.AlterField(
            model_name='windpowerplant',
            name='manufacturer',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='windpowerplant',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='windpowerplant',
            name='owner_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='windpowerplant',
            name='wind_direction',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='windpowerplant',
            name='zone',
            field=models.CharField(blank=True, choices=[("('U', 'Urban')", 'U'), ('R', 'Rural')], max_length=50, null=True),
        ),
    ]