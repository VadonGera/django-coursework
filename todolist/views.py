from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions

from .models import Task, Comment, Tag, Category
from .serializers import (
    # TaskViewSerializer,
    # TaskCreateSerializer,
    CategorySerializer,
    CommentSerializer,
    TaskSerializer,
)
from .permissions import IsAdminUser, IsOwner


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            # Разрешаем доступ для всех аутентифицированных пользователей
            permission_classes = [IsAuthenticated]
        else:
            # Разрешаем добавление, изменение и удаление только админам
            permission_classes = [IsAuthenticated, IsAdminUser]
        return [permission() for permission in permission_classes]


class TaskViewSet(viewsets.ModelViewSet):
    # queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user, is_active=True)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        task = self.get_object()
        if task.owner != self.request.user:
            raise PermissionDenied("Вы не являетесь владельцем этой задачи.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.owner != self.request.user:
            raise PermissionDenied("Вы не являетесь владельцем этой задачи.")
        # instance.delete()
        instance.is_active = False
        instance.save()


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Возвращаем только те комментарии, которые принадлежат задачам текущего пользователя
        return Comment.objects.filter(task__owner=self.request.user)

    def perform_create(self, serializer):
        task = serializer.validated_data['task']
        if task.owner != self.request.user:
            raise PermissionDenied("Вы не являетесь владельцем этой задачи.")
        serializer.save()

    def perform_update(self, serializer):
        comment = self.get_object()
        if comment.task.owner != self.request.user:
            raise PermissionDenied("Вы не являетесь владельцем этой задачи.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.task.owner != self.request.user:
            raise PermissionDenied("Вы не являетесь владельцем этой задачи.")
        instance.delete()



# class TaskListAPIView(generics.ListAPIView):
#     """Task List"""
#     serializer_class = TaskViewSerializer
#     permission_classes = [IsAuthenticated]
#
#     def get_queryset(self):
#         return Task.objects.filter(owner=self.request.user, is_active=True)
#
#
# class TaskItemAPIView(generics.RetrieveAPIView):
#     """Task Item"""
#     # queryset = Task.objects.filter(is_active=True)
#     serializer_class = TaskViewSerializer
#     permission_classes = [IsAuthenticated]
#     lookup_field = 'pk'
#
#     def get_queryset(self):
#         return Task.objects.filter(owner=self.request.user, is_active=True)
#
#
# class TaskCreateAPIView(generics.CreateAPIView):
#     """Task Create"""
#     # queryset = Task.objects.filter(is_active=True)
#     serializer_class = TaskCreateSerializer
#     permission_classes = [IsAuthenticated]  # Только аутентифицированные пользователи могут создавать задачи
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
#
#
# class TaskDeleteAPIView(generics.DestroyAPIView):
#     """Delete Task"""
#     # queryset = Task.objects.filter(owner=self.request.user, is_active=True)
#     permission_classes = [IsAuthenticated]
#     lookup_field = 'pk'
#
#     def get_queryset(self):
#         return Task.objects.filter(owner=self.request.user, is_active=True)
#
#     def perform_destroy(self, instance):
#         instance.is_active = False
#         instance.save()




# Контроллер для модели Task через ViewSet
# class TodolistViewSet(viewsets.ModelViewSet):
#     queryset = Task.objects.all()
#     serializer_class = TaskViewSerializer
#     # permission_classes = [IsAuthenticated, IsOwner]
#     # permission_classes = [IsOwner]
#
#     def perform_update(self, serializer):
#         if not serializer.instance.owner == self.request.user:
#             raise PermissionDenied("Вы не являетесь владельцем этой задачи")
#         serializer.save()
