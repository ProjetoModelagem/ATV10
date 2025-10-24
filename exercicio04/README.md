## Objetivo
Refatorar o teste de login do Exercício 01 aplicando o padrão Page Object Model (POM).

## Estrutura
- `pages/base_page.py`: classe base com métodos utilitários.
- `pages/login_page.py`: página de login.
- `pages/dashboard_page.py`: validação pós-login.
- `tests/test_login_pom.py`: teste que utiliza as páginas POM.

## Comportamento
Se o Chrome não estiver disponível no ambiente, o teste é automaticamente **pulado (skipped)**, garantindo compatibilidade.

## Como executar
```bash
pip install -r requirements.txt
```
pytest exercicios/exercicio04/tests -v

# Logs
<img width="1273" height="310" alt="exc04" src="https://github.com/user-attachments/assets/3d62fade-ee17-46b0-bdfc-c459cecc8365" />
