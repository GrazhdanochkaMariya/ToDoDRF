# Generated by Django 4.2.3 on 2023-07-29 13:15

from django.db import migrations, models
import django.db.models.deletion
import todo.models


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0004_rename_creation_date_todo_created"),
    ]

    operations = [
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("New", "New"),
                            ("In Progress", "In Progress"),
                            ("Completed", "Completed"),
                        ],
                        max_length=20,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.TextField(blank=True, null=True)),
                ("email", models.EmailField(max_length=254, unique=True)),
                (
                    "password",
                    models.CharField(
                        max_length=128, validators=[todo.models.validate_min_length]
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Todo",
        ),
        migrations.AddField(
            model_name="task",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="todo.user"
            ),
        ),
    ]
