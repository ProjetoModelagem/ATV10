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
pytest exercicios/exercicio05/tests -v