# Generated by Django 3.0.4 on 2020-03-24 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('been_and_mark', '0007_auto_20200324_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='image',
            field=models.ImageField(default='/place_pictures/iconbl.png', null=True, upload_to='place_pictures'),
        ),
    ]
