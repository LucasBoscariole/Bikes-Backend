# Generated by Django 4.1.1 on 2022-09-20 02:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bikes', '0003_alter_bikesmodel_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bikesmodel',
            old_name='rented_dates',
            new_name='is_rented',
        ),
    ]