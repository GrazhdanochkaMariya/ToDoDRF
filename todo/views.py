from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Task
from .serializers import TaskSerializer
from .permissions import IsOwnerOrReadOnly


# Get a list of all tasks.Create a new task
class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    # Set the owner of the task to the current user
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Get a list of all user's tasks
class UserTaskListView(generics.ListAPIView):
    serializer_class = TaskSerializer

    # This method helps us to get a task list for a current user
    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Task.objects.filter(user_id=user_id)


# Get information about a specific task. Update task information. Delete a task
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    # Set the owner of the task to the current user
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    # Check if user can delete a task (if he is a task-owner)
    def perform_destroy(self, instance):
        if instance.user == self.request.user:
            instance.delete()
