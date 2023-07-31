from django.contrib import admin
from django.contrib.auth.models import User

from todo.models import Task


admin.site.register(Task)

