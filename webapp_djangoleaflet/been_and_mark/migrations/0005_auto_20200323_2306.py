# Generated by Django 3.0.4 on 2020-03-23 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('been_and_mark', '0004_auto_20200323_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='image',
            field=models.ImageField(default='no_name.png', null=True, upload_to='place_pictures'),
        ),
    ]