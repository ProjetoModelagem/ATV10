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

```
# Log

<img width="1297" height="331" alt="exc01" src="https://github.com/user-attachments/assets/81789236-0402-454f-ae63-91947c37d39a" />


