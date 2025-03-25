from django.contrib import admin
from django.urls import path, include
from task.views import TaskCreateListView, TaskRetrieveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),
    # url de tarefas
    path('api/v1/', include('task.urls')), 
]
