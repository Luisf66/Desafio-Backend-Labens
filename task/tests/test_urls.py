from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from task.models import Task

class TaskUrlsTest(TestCase):
    
    def setUp(self):
        # Cria uma instância de Task para ser utilizada nos testes
        self.task_data = {
            'title': 'Test Task',
            'description': 'This is a test task description',
            'term': '2025-12-31',  # Data para o campo term
            'conclusion': '2025-12-31',  # Data para o campo conclusion
            'situation': 'N',  # Situação da tarefa
        }
        self.task = Task.objects.create(**self.task_data)
        self.task_url = reverse('task-create-list')
        self.task_detail_url = reverse('task-retrieve-update-destroy', kwargs={'pk': self.task.pk})

    def test_task_list_create_url(self):
        # Teste de POST para criação de uma nova Task
        response = self.client.post(self.task_url, data=self.task_data, content_type='application/json')
        self.assertEqual(response.status_code, 201)  # Espera-se um código 201 de sucesso (Created)

    def test_task_list_url_inclusion(self):
        # Teste de GET para a listagem de tarefas
        response = self.client.get(self.task_url)
        self.assertEqual(response.status_code, 200)  # Espera-se um código 200 de sucesso
        self.assertContains(response, self.task.title)  # Verifica se o título da tarefa está na resposta

    def test_task_detail_url(self):
        # Teste de GET para obter detalhes de uma tarefa específica
        response = self.client.get(self.task_detail_url)
        self.assertEqual(response.status_code, 200)  # Espera-se um código 200 de sucesso
        self.assertContains(response, self.task.title)  # Verifica se o título da tarefa está na resposta

    def test_task_update_url(self):
        # Teste de PUT para atualizar uma tarefa existente
        updated_data = {
            'title': 'Updated Task',
            'description': 'Updated task description',
            'term': '2026-12-31',
            'conclusion': '2026-12-31',
            'situation': 'E',
        }
        response = self.client.put(self.task_detail_url, data=updated_data, content_type='application/json')
        self.assertEqual(response.status_code, 200)  # Espera-se um código 200 de sucesso
        self.task.refresh_from_db()  # Atualiza a instância da tarefa do banco de dados
        self.assertEqual(self.task.title, updated_data['title'])  # Verifica se o título foi atualizado

    def test_task_delete_url(self):
        # Teste de DELETE para remover uma tarefa existente
        response = self.client.delete(self.task_detail_url)
        self.assertEqual(response.status_code, 204)  # Espera-se um código 204 de sucesso (No Content)
        # Verifica se a tarefa foi realmente excluída
        with self.assertRaises(Task.DoesNotExist):
            self.task.refresh_from_db()