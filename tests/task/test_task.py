import json

import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken

from todo.models import Task


@pytest.mark.django_db
def test_get_task_list(api_client, user):
    url = reverse('task-list-create')
    token = AccessToken.for_user(user)
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    Task.objects.create(title='Задача 1', status='New', user=user)
    Task.objects.create(title='Задача 2', status='In Progress', user=user)

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['results']) == 2


@pytest.mark.django_db
def test_create_new_task(api_client):
    user = User.objects.create_user(username='testuser', password='testpassword')

    url = reverse('task-list-create')
    token = AccessToken.for_user(user)
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    data = {'title': 'Новая задача', 'status': 'New', 'user': user.id}

    response = api_client.post(url, data=data, format='json')

    assert response.status_code == status.HTTP_201_CREATED
