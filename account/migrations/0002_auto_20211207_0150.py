# Generated by Django 2.2.15 on 2021-12-07 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='address',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='first_name',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='gender',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='last_name',
            field=models.CharField(max_length=60, null=True),
        ),
    ]