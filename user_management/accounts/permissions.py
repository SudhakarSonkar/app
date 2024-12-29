
from rest_framework import serializers, viewsets, permissions, status


# Permissions
class IsAdminOrOwnerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.role == 'admin':
            return True
        return obj == request.user