# Generated by Django 2.2.5 on 2020-07-04 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]