from rest_framework import serializers
from .models import BikesModel

class BikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BikesModel
        fields = ("id","name","description","owner_id","image_url","price","is_rented")
    
    def __init__(self, *args, **kwargs):
        super(BikesSerializer, self).__init__(*args, **kwargs)
        self.fields['id'].required = False
        self.fields['name'].required = False
        self.fields['description'].required = False
        self.fields['owner_id'].required = False
        self.fields['image_url'].required = False
        self.fields['price'].required = False
        self.fields['is_rented'].required = False