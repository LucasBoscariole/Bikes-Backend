from django.db import models

# Create your models here.
class UserInfo(models.Model):
     first_name = models.CharField(max_length=255)
     last_name = models.CharField(max_length=255)
     email = models.CharField(max_length=255, unique=True)
     user_id = models.IntegerField()
     image_url = models.ImageField(upload_to='photos/%Y/%m/%d',blank=True, null=True)
     zipcode = models.IntegerField(blank=True, null=True)
     street = models.CharField(max_length=255, blank=True, null=True)
     state = models.CharField(max_length=255, blank=True, null=True)