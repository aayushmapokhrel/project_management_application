from django.contrib import admin
from task.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "description",
        "status",
        "priority",
        "assigned_to"
    ]
