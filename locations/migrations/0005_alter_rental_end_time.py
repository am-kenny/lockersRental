# Generated by Django 4.2.7 on 2023-11-14 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0004_alter_locker_locker_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rental',
            name='end_time',
            field=models.DateTimeField(blank=True),
        ),
    ]
