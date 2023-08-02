from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.generics import (CreateAPIView, ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import AllowAny

from tasks.models import Task
from tasks.permissions import IsOwnerOrReadOnly
from tasks.serializers import TaskSerializer, UserSerializer


class TaskBaseAPIView(generics.GenericAPIView):
    """Base view class for tasks."""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_object(self):
        """Get a certain task by the key or raise a 404 error."""

        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.kwargs["pk"])
        return obj


class TaskDetailAPIView(TaskBaseAPIView, RetrieveUpdateDestroyAPIView):
    """View class for retrieving, updating, and deleting a single task."""

    permission_classes = [IsOwnerOrReadOnly]


class TaskListCreateAPIView(TaskBaseAPIView, ListCreateAPIView):
    """View class for retrieving a list of tasks for a user and creating a new task."""

    def get_queryset(self):
        """Return the user's task list."""

        return Task.objects.filter(user=self.request.user.id)

    def perform_create(self, serializer):
        """Save the task with the current user."""

        serializer.save(user=self.request.user)


class MarkTaskCompletedAPIView(TaskBaseAPIView, generics.UpdateAPIView):
    # """View class for marking a task as completed."""
    """Mark the task as completed and save it."""

    def perform_update(self, serializer):
        serializer.instance.status = "Completed"
        serializer.save()


class FilterTasksByStatusAPIView(TaskBaseAPIView, generics.ListAPIView):
    """View class for filtering tasks by status."""

    def get_queryset(self):
        """Return the user's tasks filtered by status."""

        status = self.request.query_params.get("status", None)
        if status is not None:
            return Task.objects.filter(user=self.request.user, status=status)
        return Task.objects.none()


class CreateUserAPIView(CreateAPIView):
    """View class for creating a new user."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
