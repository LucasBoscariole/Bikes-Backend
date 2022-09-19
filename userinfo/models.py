from django.db import models

# Create your models here.
class UserInfo(models.Model):
     first_name = models.CharField(max_length=255,blank=True, null=True)
     last_name = models.CharField(max_length=255,blank=True, null=True)
     email = models.CharField(max_length=255, unique=True,blank=True, null=True)
     user_id = models.IntegerField(blank=True, null=True)
     image_url = models.ImageField(upload_to='user_image',blank=True, null=True)
     zipcode = models.IntegerField(blank=True, null=True)
     street = models.CharField(max_length=255, blank=True, null=True)
     state = models.CharField(max_length=255, blank=True, null=True)