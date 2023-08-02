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

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from todo.views import (
    MarkTaskCompletedAPIView,
    FilterTasksByStatusAPIView,
    TaskListCreateAPIView,
    TaskDetailAPIView,
    CreateUserAPIView,
)

from django.contrib import admin
from django.urls import path, include

# Configs for Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Swagger DRF",
        default_version="v1",
        description="This is TODO ",
        terms_of_service="https://www.ourapp.com/policies/terms/",
        contact=openapi.Contact(email="contact@swaggerBlog.local"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=[
        permissions.AllowAny,
    ],
    authentication_classes=[JWTAuthentication],
)

router = routers.DefaultRouter()

urlpatterns = [
    # Swagger
    path("", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    # Admin
    path("admin/", admin.site.urls),
    # Auth
    path("api/", include(router.urls)),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    # Tasks
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
    # User
    path("users/create", CreateUserAPIView.as_view(), name="create-user"),
]
