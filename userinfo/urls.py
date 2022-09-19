from django.urls import path
from .views import UserDetailApiView, UserInfoAPIView

urlpatterns = [
 path('userinfo', UserInfoAPIView.as_view()),
 path('userinfo/<int:user_id>', UserDetailApiView.as_view()),
]