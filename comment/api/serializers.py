from rest_framework import serializers
from comment.models import Comment
from user.models import User


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())  # This should handle user as a related object

    class Meta:
        model = Comment
        fields = ["id", "content", "user", "task", "created_at"]

    def create(self, validated_data):
        # If no user is provided, use the logged-in user
        if 'user' not in validated_data:
            validated_data['user'] = self.context['request'].user  # Correctly assigns the user instance
        return super().create(validated_data)
