## Objetivo
Automatizar o teste de login na página [https://practicetestautomation.com/practice-test-login/](https://practicetestautomation.com/practice-test-login/) usando Selenium e pytest.

## Estrutura
- `test_login.py`: contém dois testes automatizados:
  - `test_login_sucesso`
  - `test_login_senha_incorreta`
- Caso o ChromeDriver não esteja disponível no ambiente, os testes são automaticamente **pulados (skipped)** com `pytest.skip()`.

## Como executar
Instale as dependências:
```bash
pip install -r requirements.txt

pytest exercicios/exercicio01/tests -v

<img width="1285" height="329" alt="image" src="https://github.com/user-attachments/assets/3c9b6fe9-dcf4-4c9f-b875-bfd26252bdf4" />
