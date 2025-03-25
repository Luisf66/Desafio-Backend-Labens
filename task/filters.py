import django_filters
from task.models import Task

class TaskFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='Title')
    description = django_filters.CharFilter(lookup_expr='icontains', label='Description')

    class Meta:
        model = Task
        fields = ['title', 'description']