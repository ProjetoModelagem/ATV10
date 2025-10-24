import pytest
import requests

emails_invalidos = [
    "sem-arroba.com",
    "@sem-usuario.com",
    "sem-dominio@",
    "espacos no meio@teste.com",
    "caracteres!especiais@teste.com",
]

@pytest.mark.parametrize("email_invalido", emails_invalidos)
def test_validacao_email_api(email_invalido):
    """
    A API reqres.in pode devolver 400 (Bad Request) OU 401 (Unauthorized)
    para cadastro/login inválido. O importante é: não pode aceitar (200).
    """
    r = requests.post(
        "https://reqres.in/api/register",
        json={"email": email_invalido, "password": "senha123"}
    )

    # O esperado para email inválido/não aceito é erro (4xx), não sucesso (200).
    assert r.status_code in (400, 401)
    assert r.status_code != 200
