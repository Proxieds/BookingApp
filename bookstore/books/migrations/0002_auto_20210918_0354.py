# Generated by Django 3.2.7 on 2021-09-18 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.FloatField(default=None),
        ),
        migrations.AddField(
            model_name='book',
            name='year',
            field=models.IntegerField(default=None),
        ),
    ]
