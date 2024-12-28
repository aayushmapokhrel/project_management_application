from rest_framework import serializers
from task.models import Task
from user.models import User


class TaskSerializer(serializers.ModelSerializer):
    assigned_to = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "status",
            "priority",
            "assigned_to",
            "project",
            "created_at",
            "due_date",
        ]

    def create(self, validated_data):
        validated_data.pop('assigned_tasks', None)
        return super().create(validated_data)