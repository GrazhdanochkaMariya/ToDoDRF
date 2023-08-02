import pytest
from django.urls import reverse
from rest_framework import status

from tasks.models import Task


@pytest.mark.django_db
def test_get_task_detail(api_client, user, authenticated_api_client):
    """Test to retrieve a specific task detail."""

    task = Task.objects.create(title="Test task", status="New", user=user)
    url = reverse("task-detail", kwargs={"pk": task.id})

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data["title"] == task.title


@pytest.mark.django_db
def test_update_task(api_client, user, authenticated_api_client):
    """Test to update a specific task."""

    task = Task.objects.create(title="Test task", status="New", user=user)
    url = reverse("task-detail", kwargs={"pk": task.id})

    updated_title = "Updated task"
    data = {"title": updated_title, "status": task.status, "user": task.user.id}

    response = api_client.put(url, data=data, format="json")

    assert response.status_code == status.HTTP_200_OK
    assert response.data["title"] == updated_title


@pytest.mark.django_db
def test_get_task_list(api_client, user, authenticated_api_client):
    """Test to retrieve a list of tasks."""

    url = reverse("task-list-create")

    Task.objects.create(title="Task1", status="New", user=user)
    Task.objects.create(title="Task2", status="In Progress", user=user)

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data["results"]) == 2


@pytest.mark.django_db
def test_create_new_task(api_client, user, authenticated_api_client):
    """Test to create a new task."""

    url = reverse("task-list-create")

    data = {"title": "New task", "status": "New", "user": user.id}

    response = api_client.post(url, data=data, format="json")

    assert response.status_code == status.HTTP_201_CREATED
    assert Task.objects.filter(title="New task", user=user).exists()


@pytest.mark.django_db
def test_delete_task(api_client, user, authenticated_api_client):
    """Test to delete a specific task."""

    task = Task.objects.create(title="Test task", status="New", user=user)
    url = reverse("task-detail", kwargs={"pk": task.id})

    response = api_client.delete(url)

    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Task.objects.filter(id=task.id).exists()


@pytest.mark.django_db
def test_mark_task_completed(api_client, user, authenticated_api_client):
    """Test to mark a task as completed."""

    task = Task.objects.create(title="Test task", status="New", user=user)
    url = reverse("mark-task-completed", kwargs={"pk": task.id})

    updated_status = "Completed"
    data = {"status": updated_status}

    response = api_client.patch(url, data=data, format="json")

    assert response.status_code == status.HTTP_200_OK
    task.refresh_from_db()
    assert task.status == updated_status


@pytest.mark.django_db
@pytest.mark.parametrize("choose_status", ["New", "In Progress", "Completed"])
def test_tasks_filter(api_client, user, choose_status, authenticated_api_client):
    """Test to filter tasks by status."""

    task_filtered = Task.objects.filter(status=choose_status)
    url = reverse("filter-tasks-by-status")

    response = api_client.get(url, {"status": choose_status})

    assert response.status_code == status.HTTP_200_OK
    assert all(task["status"] == choose_status for task in response.data["results"])


@pytest.mark.django_db
def test_get_users_tasks_list(api_client, user, authenticated_api_client):
    """Test to retrieve a list of tasks for a specific user."""

    Task.objects.create(title="Task1", status="New", user=user)
    Task.objects.create(title="Task2", status="In Progress", user=user)

    url = reverse("user-task-list", kwargs={"user_id": user.id})

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data["results"]) == 2
