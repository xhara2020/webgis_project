# Generated by Django 5.1.7 on 2025-03-17 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webgis_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='branch',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
