import random
from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from task.models import Task, SITUATION

class Command(BaseCommand):
    help = 'Popula o banco de dados com 15 tarefas'

    def handle(self, *args, **kwargs):
        # Definindo as situações possíveis
        situacoes = [situation[0] for situation in SITUATION]  # 'N', 'E', 'C', 'CA'
        
        for i in range(15):
            # Gerando título e descrição de tarefas aleatórias
            nome_tarefa = f"Tarefa {i+1}"
            descricao_tarefa = f"Descrição da Tarefa {i+1}"

            # Gerando prazos aleatórios
            hoje = timezone.now().date()
            prazo = hoje + timedelta(days=random.randint(1, 30))  # Prazo entre 1 a 30 dias
            data_conclusao = prazo + timedelta(days=random.randint(1, 15))  # Conclusão até 15 dias após o prazo

            # Gerando uma situação aleatória
            situacao = random.choice(situacoes)

            # Criando a tarefa no banco de dados
            Task.objects.create(
                title=nome_tarefa,
                description=descricao_tarefa,
                term=prazo,
                conclusion=data_conclusao,
                situation=situacao
            )
            self.stdout.write(self.style.SUCCESS(f"Tarefa {i+1} criada com sucesso!"))
