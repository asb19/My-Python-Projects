# Generated by Django 3.1.4 on 2021-01-18 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='firstName',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='secondName',
            new_name='last_name',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='favourites',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.favourite'),
        ),
    ]
