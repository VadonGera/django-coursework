from django.urls import path, include

from .apps import TodolistConfig
from .views import (
    # TaskListAPIView,
    # TaskItemAPIView,
    # TaskCreateAPIView,
    # TaskDeleteAPIView,
    CategoryViewSet,
    TaskViewSet,
    CommentViewSet,
)
from rest_framework.routers import DefaultRouter

app_name = TodolistConfig.name

urlpatterns = [
    # path('task/list/', TaskListAPIView.as_view(), name='task_list'),
    # path('task/item/<int:pk>/', TaskItemAPIView.as_view(), name='task_item'),
    # path('task/create/', TaskCreateAPIView.as_view(), name='task_create'),
    # path('task/delete/<int:pk>/', TaskDeleteAPIView.as_view(), name='task_delete'),
]

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'tasks', TaskViewSet, basename='task')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns += router.urls
