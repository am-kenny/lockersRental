# Generated by Django 4.2.7 on 2023-11-14 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0005_alter_rental_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
