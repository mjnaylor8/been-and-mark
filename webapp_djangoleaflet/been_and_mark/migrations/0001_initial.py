# Generated by Django 3.0.4 on 2020-03-22 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('place_type', models.CharField(default='Coffee Shop', max_length=100)),
                ('name', models.CharField(default='No Name', max_length=100)),
                ('latitude', models.FloatField(default=39.92)),
                ('longitude', models.FloatField(verbose_name=32.86)),
                ('notes', models.TextField()),
            ],
        ),
    ]