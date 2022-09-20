from django.db import models

# Create your models here.
class BikesModel(models.Model):
     id = models.IntegerField(auto_created = True,blank=True,primary_key=True)
     name = models.CharField(max_length=255,blank=True, null=True)
     description = models.CharField(max_length=500,blank=True, null=True)
     owner_id = models.IntegerField(blank=True, null=True)
     image_url = models.ImageField(upload_to='user_image',blank=True, null=True)
     price = models.IntegerField(blank=True, null=True)
     is_rented =  models.BooleanField(blank=True, null=True, default=False)