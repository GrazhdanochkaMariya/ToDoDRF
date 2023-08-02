import pytest
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from django.db.utils import IntegrityError


@pytest.mark.django_db
def test_create_user(api_client):
    """Test to check user creating."""

    user_data = {
        "username": "testuser",
        "password": "testpassword",
        "first_name": "Michael",
        "last_name": "Scott",
    }

    url = reverse("create-user")
    response = api_client.post(url, data=user_data, format="json")

    assert response.status_code == status.HTTP_201_CREATED

    assert User.objects.filter(username="testuser").exists()

    user = User.objects.get(username="testuser")
    assert user.first_name == "Michael"
    assert user.last_name == "Scott"


@pytest.mark.django_db
def test_unique_username():
    """Test to check uniqueness of username."""

    user1 = User.objects.create_user(
        username="Kevin", first_name="Kevin", password="password1"
    )

    with pytest.raises(IntegrityError):
        user2 = User.objects.create_user(
            username="Kevin", first_name="Kevin", password="password2"
        )
