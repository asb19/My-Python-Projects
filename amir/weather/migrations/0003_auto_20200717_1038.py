# Generated by Django 2.2.5 on 2020-07-17 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_tempvalue'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tempvalue',
            name='tempv',
        ),
        migrations.AddField(
            model_name='tempvalue',
            name='incelcius',
            field=models.BooleanField(default=False),
        ),
    ]
