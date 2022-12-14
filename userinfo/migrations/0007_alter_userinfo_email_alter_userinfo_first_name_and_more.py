# Generated by Django 4.1.1 on 2022-09-19 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0006_alter_userinfo_state_alter_userinfo_street_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='user_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
