# Generated by Django 3.0.4 on 2020-03-22 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('been_and_mark', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='latitude',
            field=models.FloatField(default=26.33685),
        ),
        migrations.AlterField(
            model_name='place',
            name='longitude',
            field=models.FloatField(default=39.49079),
        ),
    ]
