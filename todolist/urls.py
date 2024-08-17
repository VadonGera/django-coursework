from django.urls import path

from .apps import TodolistConfig
from .views import TaskListAPIView, TaskItemAPIView, TaskCreateAPIView
# from rest_framework_simplejwt.views import TokenRefreshView

app_name = TodolistConfig.name

urlpatterns = [
    path('task/list/', TaskListAPIView.as_view(), name='task_list'),
    path('task/item/<int:pk>/', TaskItemAPIView.as_view(), name='task_item'),
    path('task/create/', TaskCreateAPIView.as_view(), name='task_create'),
]
