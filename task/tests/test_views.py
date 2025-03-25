from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from task.models import Task

class TaskViewsTest(APITestCase):

    def setUp(self):
        """
        Limpa o banco de dados de tarefas antes de cada teste e cria uma tarefa para os testes.
        """
        # Limpar todas as tarefas antes de rodar o teste para garantir que estamos começando com um banco limpo
        Task.objects.all().delete()

        # Dados para a criação da task
        self.task_data = {
            'title': 'Test Task',
            'description': 'This is a test task description',
            'term': '2025-12-31',
            'conclusion': '2025-12-31',
            'situation': 'N',
        }

        # Criando uma tarefa para o teste
        self.task = Task.objects.create(**self.task_data)
        
        # URLs para os testes
        self.task_list_create_url = reverse('task-create-list')
        self.task_detail_url = reverse('task-retrieve-update-destroy', kwargs={'pk': self.task.pk})

    def test_create_task(self):
        # Teste de POST para criação de uma nova task
        response = self.client.post(self.task_list_create_url, self.task_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # Espera-se um código 201
        self.assertEqual(Task.objects.count(), 2)  # Verifica se uma nova task foi criada

    def test_list_tasks(self):
        # Teste de GET para listar as tasks
        response = self.client.get(self.task_list_create_url, format='json')
        # Imprime a resposta para debugar
        #print(response.data)  # Verifique a estrutura da resposta
        # Espera-se um código 200 (sucesso)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Verifica se a resposta contém pelo menos 1 tarefa
        self.assertGreater(len(response.data['results']), 0)  # Agora verifica a chave 'results' se existir
        # Verifica se o título da tarefa que foi criada no setUp() aparece na lista
        task_titles = [task['title'] for task in response.data['results']]  # Acessando a lista corretamente
        self.assertIn(self.task.title, task_titles)  # Verifica se a task criada está na lista de tarefas


    def test_retrieve_task(self):
        # Teste de GET para detalhes de uma tarefa específica
        response = self.client.get(self.task_detail_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Espera-se um código 200
        self.assertEqual(response.data['title'], self.task.title)  # Verifica se o título da tarefa está correto

    def test_update_task(self):
        # Teste de PUT para atualizar uma tarefa existente
        updated_data = {
            'title': 'Updated Task',
            'description': 'Updated task description',
            'term': '2026-12-31',
            'conclusion': '2026-12-31',
            'situation': 'E',
        }
        response = self.client.put(self.task_detail_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Espera-se um código 200
        self.task.refresh_from_db()  # Atualiza a instância da tarefa do banco de dados
        self.assertEqual(self.task.title, updated_data['title'])  # Verifica se o título foi atualizado

    def test_delete_task(self):
        # Teste de DELETE para excluir uma tarefa existente
        response = self.client.delete(self.task_detail_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)  # Espera-se um código 204 (No Content)
        # Verifica se a tarefa foi excluída
        with self.assertRaises(Task.DoesNotExist):
            self.task.refresh_from_db()

    def test_create_task_missing_title(self):
        """
        Testa se a API retorna erro ao tentar criar uma tarefa sem o campo 'title'.
        """
        invalid_task_data = {
            'description': 'This task has no title',
            'term': '2025-12-31',
            'conclusion': '2025-12-31',
            'situation': 'N',
        }
        response = self.client.post(self.task_list_create_url, invalid_task_data, format='json')
        # Espera-se um código 400 Bad Request
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # Verifica se a resposta contém um erro referente ao campo 'title'
        self.assertIn('title', response.data)

    @classmethod
    def tearDownClass(cls):
        """
        Limpa os dados após a execução dos testes para garantir que o banco de dados esteja completamente limpo.
        """
        Task.objects.all().delete()
        super().tearDownClass()
