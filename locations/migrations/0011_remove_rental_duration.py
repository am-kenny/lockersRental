# Generated by Django 4.2.7 on 2023-11-14 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0010_rental_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rental',
            name='duration',
        ),
    ]
