# Generated by Django 3.1.6 on 2021-03-18 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210318_2002'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendencedata',
            old_name='time',
            new_name='entry_time',
        ),
        migrations.AddField(
            model_name='attendencedata',
            name='exit_Time',
            field=models.TimeField(null=True),
        ),
    ]