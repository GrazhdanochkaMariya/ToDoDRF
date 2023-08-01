import pytest
from django.db.utils import IntegrityError
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_create_user():
    user = User.objects.create_user(username='testuser', password='testpassword', first_name='Michael', last_name='Scott')

    assert User.objects.count() == 1
    assert User.objects.first().username == 'testuser'
    assert User.objects.first().first_name == 'Michael'
    assert User.objects.first().last_name == 'Scott'


@pytest.mark.django_db
def test_unique_username():
    user1 = User.objects.create_user(
        username='user2',
        first_name='John',
        password='password1'
    )

    with pytest.raises(IntegrityError):
        user2 = User.objects.create_user(
            username='user2',
            first_name='Jane',
            password='password2'
        )


