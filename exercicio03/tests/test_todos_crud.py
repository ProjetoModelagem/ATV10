import requests

BASE_URL = "https://jsonplaceholder.typicode.com/todos"

def test_crud_todos():
    # CREATE
    novo = {
        "title": "Minha tarefa",
        "completed": False,
        "userId": 1
    }
    r = requests.post(BASE_URL, json=novo)
    assert r.status_code == 201  # JSONPlaceholder responde 201 no POST
    todo = r.json()

    todo_id = todo.get("id", None)
    assert todo_id is not None

    # READ (pode não existir de verdade no servidor)
    r = requests.get(f"{BASE_URL}/{todo_id}")

    # Aqui aceitamos dois cenários válidos:
    # - 200: o recurso existe (alguns ambientes mockados fazem isso)
    # - 404: o recurso não foi realmente persistido (comportamento real do JSONPlaceholder)
    assert r.status_code in (200, 404)

    # UPDATE (PATCH)
    r_patch = requests.patch(f"{BASE_URL}/{todo_id}", json={"completed": True})
    assert r_patch.status_code in (200, 201)
    body_patch = r_patch.json()
    assert body_patch.get("completed") is True

    # DELETE
    r_delete = requests.delete(f"{BASE_URL}/{todo_id}")
    # JSONPlaceholder costuma devolver 200 ou 204
    assert r_delete.status_code in (200, 204)

    # VERIFY (leitura depois do delete)
    r_verify = requests.get(f"{BASE_URL}/{todo_id}")
    # De novo: aceitar os dois cenários (se ele não persistiu ou já "apagou")
    assert r_verify.status_code in (200, 404)
