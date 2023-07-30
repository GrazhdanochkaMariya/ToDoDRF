from django.http import HttpResponse
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

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


# Marking a task as completed
class MarkTaskCompletedView(APIView):
    def patch(self, request, task_id):
        try:
            task = Task.objects.get(pk=task_id)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        task.status = 'Completed'
        task.save()
        serializer = TaskSerializer(task)
        return Response(serializer.data)


# Filtering tasks by status
class FilterTasksByStatusView(APIView):
    def get(self, request):
        status_param = request.query_params.get('status', None)
        if status_param is not None:
            tasks = Task.objects.filter(status=status_param)
        else:
            tasks = Task.objects.all()

        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
