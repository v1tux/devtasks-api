# DevTasks API

API de gerenciamento de tarefas desenvolvida com Python, FastAPI e SQLAlchemy.

Este projeto está sendo construído com foco em aprendizado prático de desenvolvimento backend, arquitetura em camadas, banco de dados, APIs REST e boas práticas de mercado.

## Tecnologias utilizadas

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn
- Git/GitHub

## Funcionalidades atuais

- Criar tarefas
- Listar tarefas
- Buscar tarefa por ID
- Atualizar tarefas
- Deletar tarefas
- Persistência com banco SQLite
- Documentação automática com Swagger
- Arquitetura com routes, schemas, models, services e database

## Estrutura do projeto

```txt
app/
├── database/
│   ├── base.py
│   └── connection.py
├── models/
│   └── task.py
├── routes/
│   └── tasks.py
├── schemas/
│   └── task.py
├── services/
│   └── task_service.py
└── main.py

## Rodando com Docker

Crie a imagem:

```bash
docker build -t devtasks-api .

Execute o container:

docker run -p 8000:8000 devtasks-api

Acesse:

http://127.0.0.1:8000/docs