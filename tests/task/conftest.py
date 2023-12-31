import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import AccessToken


@pytest.fixture
def api_client():
    """Fixture for creating an unauthenticated APIClient instance."""
    return APIClient()


@pytest.fixture
def user():
    """Fixture for creating a test user."""
    return User.objects.create_user(
        username="testuser",
        password="testpassword",
        first_name="Test",
        last_name="User",
    )


@pytest.fixture
def authenticated_api_client(api_client, user):
    """Fixture for creating an authenticated APIClient instance."""
    token = AccessToken.for_user(user)
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    return api_client
