# Generated by Django 3.0.4 on 2020-03-23 23:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('been_and_mark', '0003_place_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='place',
            name='latitude',
            field=models.FloatField(default=39.49079),
        ),
        migrations.AlterField(
            model_name='place',
            name='longitude',
            field=models.FloatField(default=26.33685),
        ),
    ]
