from rest_framework import serializers
from .models import Task, Comment, Tag, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'color', ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'task', 'comment', 'created_at']


class TaskSerializer(serializers.ModelSerializer):
    comments_count = serializers.IntegerField(source='comments.count', read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'category', 'status', 'owner',
            'tags', 'is_active', 'due_date', 'comments_count', 'comments'
        ]
        read_only_fields = ['owner']
