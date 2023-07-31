import pytest
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError
from django.contrib.auth.models import User



@pytest.mark.django_db
def test_create_user_with_valid_credentials():
    user = User.objects.create_user(username='testuser', password='testpassword', first_name='Masha')
    assert user.username == 'testuser'
    assert user.check_password('testpassword')
    assert user.first_name == 'Masha'


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


# @pytest.mark.django_db
# def test_create_user_with_short_password():
#     User = get_user_model()
#     user = User.objects.create_user(username='user123', first_name='Masha', password='6')


@pytest.mark.django_db
def test_create_superuser():
    User = get_user_model()
    admin_user = User.objects.create_superuser(email='test_superuser@test.com', username='super_user',
                                               password='superuser', )
    assert admin_user.is_active == True
    assert admin_user.is_staff == True
    assert admin_user.is_superuser == True
