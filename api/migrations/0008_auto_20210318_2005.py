# Generated by Django 3.1.6 on 2021-03-18 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20210318_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendencedata',
            name='exit_Time',
            field=models.TimeField(default=None, null=True),
        ),
    ]
