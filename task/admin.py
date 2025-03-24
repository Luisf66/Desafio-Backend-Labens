from django.contrib import admin
from .models import Task

@admin.register(Task)
# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'term', 'conclusion', 'situation')