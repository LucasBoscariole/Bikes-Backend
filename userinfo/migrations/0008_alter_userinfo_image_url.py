# Generated by Django 4.1.1 on 2022-09-19 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0007_alter_userinfo_email_alter_userinfo_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='image_url',
            field=models.ImageField(blank=True, null=True, upload_to='user_image'),
        ),
    ]