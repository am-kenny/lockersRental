# Generated by Django 4.2.7 on 2023-11-14 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0006_alter_rental_end_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='rental',
            name='is_rented',
            field=models.BooleanField(default=True),
        ),
    ]
