# Generated by Django 2.2.5 on 2019-09-20 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0003_destination_newprice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destination',
            name='newprice',
        ),
    ]
