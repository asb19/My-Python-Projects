# Generated by Django 2.2.5 on 2020-03-23 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20200323_0153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headline',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='newscollection/images'),
        ),
    ]