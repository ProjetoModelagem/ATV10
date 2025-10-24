## Membros
- Guilherme de Abreu – 22.222.028-7  
- Kaique Fernandes – 22.221.011-4  

## Execução dos Testes

Ambiente: Windows 10, Python 3.12, pytest 7.4.3

### Resultados obtidos:

- exercicio01 (testes Web com Selenium / login):
  - 2 skipped  
  - Motivo: ambiente sem Chrome instalado. Esse comportamento é esperado e foi tratado no teste usando pytest.skip().

- exercicio02 (API Fake Store):
  - 3 passed

- exercicio03 (CRUD JSONPlaceholder /todos):
  - 1 passed  
  - Observação: os testes aceitam 404 em GET após POST/DELETE porque o JSONPlaceholder não persiste os dados de verdade, ele só simula.

- exercicio04 (Page Object Model - POM):
  - 1 skipped  
  - Motivo: sem Chrome. O teste tenta abrir navegador; se não conseguir, chama pytest.skip() em vez de falhar.

- exercicio05:
  - test_validacoes_parametrizadas.py (validação de e-mail inválido, via reqres.in): passed  

  - test_busca_parametrizada.py (busca no Google): skipped (sem Chrome)

 # Os logs estão dentro de cada readme em cada exercicio
