# Generated by Django 3.1.6 on 2021-03-18 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20210318_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendencedata',
            name='status',
            field=models.CharField(choices=[('inschool', 'Currently In School'), ('left', 'Left The School')], default='inschool', max_length=20),
        ),
    ]