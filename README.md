# Desafio-Backend-Labens

Este projeto consiste na criação de uma API para o gerenciamento de tarefas (to-do list). A API permite aos usuários realizar operações CRUD (criar, ler, atualizar e excluir) em tarefas, com funcionalidades adicionais como busca e paginação.

## Tecnologias Utilizadas

- Django
- Django Rest Framework
- SQLite (Banco de dados)
- Docker (Opcional para ambiente de container)
- Postman/Insomnia (Ferramentas para testes da API)

## Requisitos Funcionais

- **Listar tarefas:** A API deve permitir listar todas as tarefas com paginação (5 tarefas por vez).
- **Buscar tarefas:** A busca deve ser feita no título e na descrição das tarefas.
- **Criar uma tarefa:** Permitir criar uma nova tarefa.
- **Visualizar uma tarefa:** Permitir visualizar os detalhes de uma tarefa.
- **Atualizar uma tarefa:** Permitir editar os dados de uma tarefa existente.
- **Excluir uma tarefa:** Permitir excluir uma tarefa.

Cada tarefa possui os seguintes campos:
- Título (máximo de 100 caracteres)
- Descrição (opcional, máximo de 250 caracteres)
- Prazo (data)
- Data de Conclusão (data)
- Situação (enum: 'Nova', 'Em andamento', 'Concluída', 'Cancelada')

## Disposição das urls

    
- **GET** /api/v1/task/ - Listar todas as tarefas

    
- **GET** /api/v1/task/id/ - Visualizar uma tarefa específica

    
- **POST** /api/v1/task/ - Criar uma nova tarefa

    
- **PATCH** /api/v1/task/id/ - Atualizar uma tarefa

    
- **DELETE** /api/v1/task/id/ - Excluir uma tarefa

    
- **GET** /api/v1/task/?title=EXEMPLO - Buscar tarefas por título
    
    
- **GET** /api/v1/task/?description=EXEMPLO - Buscar tarefas por descrição

## Como Rodar o Projeto

### 1. Instalar dependências

```bash
pip install -r requirements.txt
```
### 2. Migrar o banco de dados
```bash
python3 manage.py migrate
```

### 3. Rodar o servidor de desenvolvimento
```bash
python3 manage.py runserver
```
