# Generated by Django 4.2.7 on 2023-11-14 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0007_rental_is_rented'),
    ]

    operations = [
        migrations.AddField(
            model_name='locker',
            name='is_locked',
            field=models.BooleanField(default=False),
        ),
    ]
