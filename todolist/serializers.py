from rest_framework import serializers

from .models import Task, Comment, Tag, Category


# Сериализатор для тегов Category
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'color',]


# Сериализатор для Task_List и Task_Item
class TaskViewSerializer(serializers.ModelSerializer):
    # кол-во комментариев у задачи
    comments_count = serializers.IntegerField(source='comments.all.count', read_only=True)
    category = CategorySerializer()

    class Meta:
        model = Task
        fields = [
            'id',
            'title',
            'description',
            'category',
            'due_date',
            'status',
            'tags',
            'comments_count',
        ]


# Сериализатор для Task_Create
class TaskCreateSerializer(serializers.ModelSerializer):
    # кол-во комментариев у задачи
    # comments_count = serializers.IntegerField(source='comments.all.count', read_only=True)
    # category = CategorySerializer()

    class Meta:
        model = Task
        fields = '__all__'
        # fields = [
        #     'id',
        #     'title',
        #     'description',
        #     'category',
        #     'due_date',
        #     'status',
        #     'tags',
        #     'comments_count',
        # ]
