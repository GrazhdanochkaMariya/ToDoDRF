from rest_framework import permissions


# Permission class
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Only-read mode
        if request.method in permissions.SAFE_METHODS:
            return True

        # Execute all the requests. Permissions for task-owner
        return obj.user == request.user