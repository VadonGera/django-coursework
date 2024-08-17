from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions

from .models import Task, Comment, Tag, Category
from .serializers import TaskViewSerializer, TaskCreateSerializer

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Проверяем, что пользователь является владельцем объекта
        return obj.owner == request.user


class TaskListAPIView(generics.ListAPIView):
    """Task List"""
    queryset = Task.objects.all()
    serializer_class = TaskViewSerializer


class TaskItemAPIView(generics.RetrieveAPIView):
    """Task Item"""
    queryset = Task.objects.all()
    serializer_class = TaskViewSerializer
    lookup_field = 'pk'


class TaskCreateAPIView(generics.CreateAPIView):
    """Task Create"""
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer


# Контроллер для модели Task через ViewSet
class TodolistViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskViewSerializer
    # permission_classes = [IsAuthenticated, IsOwner]
    # permission_classes = [IsOwner]

    def perform_update(self, serializer):
        if not serializer.instance.owner == self.request.user:
            raise PermissionDenied("Вы не являетесь владельцем этой задачи")
        serializer.save()
