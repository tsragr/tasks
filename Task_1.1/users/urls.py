from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
# from users.views import UserViewSet,
from users.views import get_post_users, get_delete_update_user

# router = DefaultRouter()
# router.register(r'users', UserViewSet, basename='user')

# urlpatterns = router.urls

urlpatterns = [
    path('user/<pk>/', get_delete_update_user, name='get_delete_update_user'),
    path('users/', get_post_users, name='get_post_users')
]
