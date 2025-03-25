from django.contrib import admin
from django.urls import path
from task.views import TaskCreateListView, TaskRetrieveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task/', TaskCreateListView.as_view(), name='task-create-list'),
    path('task/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-retrieve-update-destroy'),  
]
