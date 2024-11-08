from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Таск."""

    class Meta:
        """Мета."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
