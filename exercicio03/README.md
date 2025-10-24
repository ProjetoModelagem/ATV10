## Objetivo
Validar operações CRUD (Create, Read, Update, Delete) em uma API REST fake.

## Estrutura
- `test_todos_crud.py`: executa as operações CRUD no endpoint https://jsonplaceholder.typicode.com/todos.
- O teste aceita status code 404 nos `GET` porque o JSONPlaceholder não persiste dados de verdade.

## Como executar
```bash
pip install -r requirements.txt
pytest exercicios/exercicio03/tests -v