from rest_framework import permissions


class IsStaffUser(permissions.IsAdminUser):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)