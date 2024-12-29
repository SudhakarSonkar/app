from rest_framework.routers import DefaultRouter
from accounts.views import UserViewSet
from rest_framework.routers import DefaultRouter
from .views import RegisterView, LoginView
from django.urls import path, include

router = DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('', include(router.urls)),
]