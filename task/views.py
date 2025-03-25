from task.models import Task
from rest_framework import generics
from task.serializers import TaskSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import TaskFilter

class TaskCreateListView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TaskFilter

class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer