# Generated by Django 4.0.4 on 2022-05-04 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_remove_todo_duration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='creation_date',
            new_name='created',
        ),
    ]