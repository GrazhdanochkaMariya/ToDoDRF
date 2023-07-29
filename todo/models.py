from django.db import models
from django.core.exceptions import ValidationError


# Minimal length chars validator
def validate_min_length(value, min_length=6):
    if len(value) < min_length:
        raise ValidationError(
            f'The password should be at least {min_length} characters long.',
            params={'min_length': min_length},
        )


# Model for users
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.TextField(blank=True, null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, validators=[validate_min_length])

    def __str__(self):
        return self.first_name


# Model for tasks
class Task(models.Model):
    # Choice tuples for status. First index for db savings, second for displaying.
    STATUS_CHOICES = [
        ('New', 'New'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title