# Generated by Django 4.1.1 on 2022-09-19 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0004_alter_userinfo_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='state',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='street',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='zipcode',
            field=models.IntegerField(blank=True),
        ),
    ]
