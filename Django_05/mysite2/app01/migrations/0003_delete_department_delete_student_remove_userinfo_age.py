# Generated by Django 4.2.9 on 2024-01-31 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_department_student'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='age',
        ),
    ]
