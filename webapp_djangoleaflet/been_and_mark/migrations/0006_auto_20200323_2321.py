# Generated by Django 3.0.4 on 2020-03-23 23:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('been_and_mark', '0005_auto_20200323_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
