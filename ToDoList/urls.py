from django.urls import path
from ToDoList.views import TaskAPIView, TasksAPIView


urlpatterns = [
    path('task/', TasksAPIView.as_view(), name='Tasks'),
    path('task/<int:pk>/', TaskAPIView.as_view(), name='Task')
]