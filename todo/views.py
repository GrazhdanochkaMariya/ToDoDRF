from rest_framework import generics
from django.shortcuts import get_object_or_404

from todo.models import Task
from todo.serializers import TaskSerializer


# Custom base view class
class TaskBaseAPIView(generics.GenericAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    # Get certain  task by the key or 404 error
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.kwargs['pk'])
        return obj


# View class for tasks CRUD operations
class TaskAPIView(TaskBaseAPIView, generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):

    # User`s task list
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    # Save the task
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# View class for marking 'completed'
class MarkTaskCompletedAPIView(TaskBaseAPIView, generics.UpdateAPIView):

    # Mark the task as completed and save it
    def perform_update(self, serializer):
        serializer.instance.status = 'Completed'
        serializer.save()


# View class for filtering tasks by status
class FilterTasksByStatusAPIView(TaskBaseAPIView, generics.ListAPIView):

    # Get the task list with certain status
    def get_queryset(self):
        status = self.request.query_params.get('status', None)
        if status is not None:
            return Task.objects.filter(user=self.request.user, status=status)
        return Task.objects.none()
