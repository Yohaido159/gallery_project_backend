from rest_framework import permissions
from rest_auth.registration.views import SocialLoginView


class ListGalleryPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return True


class DetailGalleryPermissions(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if obj.is_paid == False:
            return True
        return False
