from django.urls import path
from .views import PostView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('posts/', PostView.as_view(), name='post_view'),
    path('token/', TokenObtainPairView.as_view()),
    path('token-refresh/', TokenRefreshView.as_view())
]
