from django.urls import path
from . import views

urlpatterns = [
    # url listar e cadastrar tarefas
    path('task/', views.TaskCreateListView.as_view(), name='task-create-list'),
    # url para visualizar, editar e deletar tarefas
    path('task/<int:pk>/', views.TaskRetrieveUpdateDestroyView.as_view(), name='task-retrieve-update-destroy'),  
]
