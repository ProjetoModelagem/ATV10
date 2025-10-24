## Objetivo
Validar operações CRUD (Create, Read, Update, Delete) em uma API REST fake.

## Estrutura
- `test_todos_crud.py`: executa as operações CRUD no endpoint https://jsonplaceholder.typicode.com/todos.
- O teste aceita status code 404 nos `GET` porque o JSONPlaceholder não persiste dados de verdade.

## Como executar
```bash
pip install -r requirements.txt
```
pytest exercicios/exercicio03/tests -v

# Logs
<img width="1283" height="311" alt="exc03" src="https://github.com/user-attachments/assets/b12f9fdb-543b-4c06-b427-d07f4fd1cf01" />
