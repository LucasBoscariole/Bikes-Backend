from django.urls import path
from .views import BikeByOwnerIdAPIView, BikeSingleApiView, BikesAPIView

urlpatterns = [
 path('bikes', BikesAPIView.as_view()),
 path('bikes/<int:bike_id>', BikeSingleApiView.as_view()),
 path('bikes/owner-id/<int:id>', BikeByOwnerIdAPIView.as_view()),
]