# Generated by Django 4.2.9 on 2024-01-31 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_userinfo_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='data',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='size',
        ),
    ]
