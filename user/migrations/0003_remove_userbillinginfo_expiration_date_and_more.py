# Generated by Django 4.2.7 on 2023-11-11 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_rename_address_userbillingaddress_house_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userbillinginfo',
            name='expiration_date',
        ),
        migrations.AddField(
            model_name='userbillinginfo',
            name='expiration_month',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userbillinginfo',
            name='expiration_year',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]