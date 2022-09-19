from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserInfo
from .serializers import UserInfoSerializer
from rest_framework import status

# Create your views here.
class UserInfoAPIView(APIView):
    def get(self, request):
        todos = UserInfo.objects.all()
        serializer = UserInfoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = {
            "first_name": request.data.get('first_name'),
            "last_name": request.data.get('last_name'),
            "email": request.data.get('email'),
            "user_id": request.data.get('user_id'),
            "image_url": request.data.get('image_url'),
            "zipcode": request.data.get('zipcode'),
            "street": request.data.get('street'),
            "state": request.data.get('state'),
        }
        serializer = UserInfoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailApiView(APIView):
    
    def get_object(self, user_id):
        try:
            return UserInfo.objects.get(user_id=user_id)
        except UserInfo.DoesNotExist:
            return None
    
    def get(self, request, user_id, *args, **kwargs):
        
        user_instance = self.get_object(user_id)
        if not user_instance:
            return Response(
                {"res": 'No user with this Id.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = UserInfoSerializer(user_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, user_id, *args, **kwargs):
        user_instance = self.get_object(user_id)
        if not user_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = request.data
        serializer = UserInfoSerializer(instance = user_instance, data=data, partial  = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
