## Objetivo
Aplicar testes parametrizados com pytest em dois contextos:
1. Validação de e-mails inválidos (API pública Reqres)
2. Busca automatizada no Google (Selenium)

## Estrutura
- `test_validacoes_parametrizadas.py`: testa 5 formatos inválidos de e-mails.
- `test_busca_parametrizada.py`: realiza buscas no Google (puladas caso não haja Chrome disponível).

## Como executar
```bash
pip install -r requirements.txt
```
pytest exercicios/exercicio05/tests -v

# Logs
<img width="1275" height="400" alt="exc05" src="https://github.com/user-attachments/assets/4225e9fa-102d-405c-806c-969be2fa1a5a" />


<img width="1274" height="355" alt="exc05_2" src="https://github.com/user-attachments/assets/22cd0a4f-a89d-49da-a072-f0296cd96463" />
