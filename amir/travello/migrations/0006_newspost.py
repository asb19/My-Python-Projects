# Generated by Django 2.2.5 on 2019-10-10 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0005_auto_20191008_1121'),
    ]

    operations = [
        migrations.CreateModel(
            name='newspost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('text', models.TextField()),
                ('date', models.DateField(null=True)),
                ('month', models.CharField(max_length=10)),
            ],
        ),
    ]
