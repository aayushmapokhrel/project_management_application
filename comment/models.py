from django.db import models
from user.models import User


class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE

        )
    task = models.ForeignKey(
        "task.Task", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:50]
