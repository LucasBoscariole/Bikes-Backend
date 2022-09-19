from rest_framework import serializers
from .models import UserInfo

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ["first_name","last_name","email","user_id","image_url","zipcode","street","state"]
        
    def __init__(self, *args, **kwargs):
        super(UserInfoSerializer, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = False
        self.fields['last_name'].required = False
        self.fields['email'].required = False
        self.fields['user_id'].required = False
        self.fields['image_url'].required = False
        self.fields['zipcode'].required = False
        self.fields['street'].required = False
        self.fields['state'].required = False