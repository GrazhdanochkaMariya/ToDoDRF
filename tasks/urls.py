from django.urls import path
from rest_framework import routers

from tasks.views import (FilterTasksByStatusAPIView, MarkTaskCompletedAPIView,
                         TaskDetailAPIView, TaskListCreateAPIView)

router = routers.DefaultRouter()

urlpatterns = [  # Tasks
    # Get a list of all tasks. Create a new task.
    path("tasks/", TaskListCreateAPIView.as_view(), name="task-list-create"),
    # Get a list of all user's tasks.
    path(
        "tasks/user/<int:user_id>/",
        TaskListCreateAPIView.as_view(),
        name="user-task-list",
    ),
    # Get information about a specific task. Update task information. Delete a task.
    path("tasks/<int:pk>/", TaskDetailAPIView.as_view(), name="task-detail"),
    # Marking a task as completed
    path(
        "tasks/<int:pk>/mark-completed/",
        MarkTaskCompletedAPIView.as_view(),
        name="mark-task-completed",
    ),
    # Filtering tasks by status
    path(
        "tasks/filter/",
        FilterTasksByStatusAPIView.as_view(),
        name="filter-tasks-by-status",
    ),
]
