from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Custom permission class that allows only the owner of a task to modify it."""

    def has_object_permission(self, request, view, obj):
        """Check if the user has permission to perform the given action on the task."""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user
