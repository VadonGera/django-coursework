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

# class TaskViewSerializer(serializers.ModelSerializer):
#     # кол-во комментариев у задачи
#     comments_count = serializers.IntegerField(source='comments.all.count', read_only=True)
#     category = CategorySerializer()
#
#     class Meta:
#         model = Task
#         fields = ['id', 'title', 'description', 'category', 'due_date', 'status', 'tags', 'comments_count',]
#
#
# class TaskCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Task
#         fields = ['id', 'title', 'description', 'category', 'due_date', 'status', 'tags',]
