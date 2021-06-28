from django.urls import path
from .views import PostView, register_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', register_view, name='register'),
    path('posts/', PostView.as_view(), name='post_view'),
    path('token/', TokenObtainPairView.as_view()),
    path('token-refresh/', TokenRefreshView.as_view())
]
