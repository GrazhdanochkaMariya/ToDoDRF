"""TodoWoo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)

from todo.views import TaskListCreateView, UserTaskListView, TaskDetailView, MarkTaskCompletedView, \
    FilterTasksByStatusView

from django.contrib import admin
from django.urls import path


urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Auth
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # Tasks
    # Get a list of all tasks. Create a new task.
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    # Get a list of all user's tasks.
    path('tasks/user/<int:user_id>/', UserTaskListView.as_view(), name='user-task-list'),
    # Get information about a specific task. Update task information. Delete a task.
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    # Marking a task as completed
    path('tasks/<int:task_id>/mark-completed/', MarkTaskCompletedView.as_view(), name='mark-task-completed'),
    # Filtering tasks by status
    path('tasks/filter/', FilterTasksByStatusView.as_view(), name='filter-tasks-by-status'),

]
