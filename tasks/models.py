from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    """Model representing a task."""

    # Choice tuples for status. First index for db savings, second for displaying.
    STATUS_CHOICES = [
        ("New", "New"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """String representation of the task object."""

        return self.title
