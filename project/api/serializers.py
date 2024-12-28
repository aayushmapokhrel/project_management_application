from rest_framework import serializers
from project.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "name", "description", "owner", "created_at"]

    def create(self, validated_data):
        created_by = validated_data.pop("created_by", None)
        project = Project.objects.create(**validated_data)
        if created_by:
            project.created_by = created_by
            project.save()
        return project
