from .models import BikesModel
from .serializers import BikesSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.
class BikesAPIView(APIView):
     serializer_class = BikesSerializer
     
     def get(self, request, format=None):
        users = BikesModel.objects.all()
        serializer = BikesSerializer(users, many=True)
        return Response(serializer.data)
       
     def post(self, request, *args, **kwargs):
        serializer = BikesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BikeSingleApiView(APIView):
    serializer_class = BikesSerializer
     
    def get_object(self, bike_id):
        try:
            return BikesModel.objects.get(id=bike_id)
        except BikesModel.DoesNotExist:
            return None
    
    def get(self, request, bike_id, *args, **kwargs):
        user_instance = self.get_object(bike_id)
        if not user_instance:
            return Response(
                {"res": 'No user with this Id.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = BikesSerializer(user_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, bike_id, *args, **kwargs):
        user_instance = self.get_object(bike_id)
        if not user_instance:
            return Response(
                {"res": "Object with this id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = request.data
        serializer = BikesSerializer(instance = user_instance, data=data, partial  = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, bike_id, *args, **kwargs):
        todo_instance = self.get_object(bike_id)
        
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        todo_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )

class BikeByOwnerIdAPIView(APIView):
    serializer_class = BikesSerializer
    
    def get(self, request, id, *args, **kwargs):
        user_instance = BikesModel.objects.filter(owner_id=id)
        if not user_instance:
            return Response(
                {"res": 'No bicycle created from this user.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = BikesSerializer(user_instance, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)