# Generated by Django 3.1.6 on 2021-03-18 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schoolregistration',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='schoolregistration',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='schoolregistration',
            name='username',
        ),
    ]