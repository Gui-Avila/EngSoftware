# User Stories — FinTrack

> Histórias de usuário detalhadas com critérios de aceitação, subtasks e
> rastreabilidade até o código.

---

## HU-01 — Registrar Transação Financeira

| Campo | Valor |
|---|---|
| **ID** | HU-01 |
| **Épico** | EP-02 — Gestão de Transações |
| **Feature** | FT-03 — Registro de Transações |
| **Story Points** | 5 |
| **Prioridade** | Must Have |
| **Sprint** | Sprint 1 |
| **Status** | ✅ Done |

### Narrativa

> **Como** usuário do FinTrack,
> **quero** registrar uma transação financeira (entrada ou saída),
> **para que** eu possa manter um histórico das minhas movimentações.

### Critérios de Aceitação

- [x] CA-01: O sistema deve aceitar descrição, valor, tipo (ENTRADA/SAIDA),
  categoria e data opcional.
- [x] CA-02: O valor deve ser positivo (> 0); caso contrário, retornar erro
  `ValorInvalidoError`.
- [x] CA-03: A descrição não pode ser vazia; caso contrário, retornar erro
  `DescricaoVaziaError`.
- [x] CA-04: O tipo deve ser ENTRADA ou SAIDA; caso contrário, retornar erro
  `TipoInvalidoError`.
- [x] CA-05: A categoria informada deve existir no sistema; caso contrário,
  retornar erro `CategoriaInexistenteError`.
- [x] CA-06: Se a data não for informada, usar a data atual.
- [x] CA-07: A transação criada deve ser persistida no banco de dados.
- [x] CA-08: O endpoint `POST /transacoes` deve retornar status 201 com o JSON
  da transação criada.

### Subtasks

| ID | Subtask | Responsável | Status |
|---|---|---|---|
| HU-01-T1 | Criar entidade `Transacao` com validações | Dev | ✅ Done |
| HU-01-T2 | Criar enum `TipoTransacao` (ENTRADA/SAIDA) | Dev | ✅ Done |
| HU-01-T3 | Criar exceções de domínio | Dev | ✅ Done |
| HU-01-T4 | Criar interface `TransacaoRepository` (ABC) | Dev | ✅ Done |
| HU-01-T5 | Implementar use case `CriarTransacao` | Dev | ✅ Done |
| HU-01-T6 | Implementar `TransacaoRepositorySQLite` | Dev | ✅ Done |
| HU-01-T7 | Criar rota `POST /transacoes` | Dev | ✅ Done |
| HU-01-T8 | Escrever testes unitários (domínio + use case) | Dev | ✅ Done |

### Rastreabilidade

| Artefato | Arquivo |
|---|---|
| Entidade | `domain/entities/transacao.py` |
| Exceções | `domain/exceptions.py` |
| Interface | `use_cases/interfaces/transacao_repository.py` |
| Use Case | `use_cases/criar_transacao.py` |
| Repositório | `infra/repositories/transacao_repository_sqlite.py` |
| Rota | `app/routes/transacao_routes.py` |
| Testes domínio | `tests/domain/test_transacao.py` (11 testes) |
| Testes use case | `tests/use_cases/test_criar_transacao.py` (6 testes) |

---

## HU-02 — Criar Categoria de Transação

| Campo | Valor |
|---|---|
| **ID** | HU-02 |
| **Épico** | EP-01 — Gestão de Categorias |
| **Feature** | FT-01 — Cadastro de Categorias |
| **Story Points** | 3 |
| **Prioridade** | Must Have |
| **Sprint** | Sprint 1 |
| **Status** | ✅ Done |

### Narrativa

> **Como** usuário do FinTrack,
> **quero** criar categorias para organizar minhas transações,
> **para que** eu possa classificar minhas entradas e saídas por tipo
> (ex.: Alimentação, Transporte, Salário).

### Critérios de Aceitação

- [x] CA-01: O sistema deve aceitar nome da categoria e limite mensal
  (opcional).
- [x] CA-02: O nome não pode ser vazio; caso contrário, retornar erro
  `NomeVazioError`.
- [x] CA-03: Se informado, o limite mensal deve ser >= 0; caso contrário,
  retornar erro `LimiteInvalidoError`.
- [x] CA-04: A categoria criada deve ser persistida no banco de dados.
- [x] CA-05: O endpoint `POST /categorias` deve retornar status 201 com o JSON
  da categoria criada.
- [x] CA-06: O endpoint `GET /categorias` deve listar todas as categorias
  cadastradas.

### Subtasks

| ID | Subtask | Responsável | Status |
|---|---|---|---|
| HU-02-T1 | Criar entidade `Categoria` com validações | Dev | ✅ Done |
| HU-02-T2 | Criar exceções `NomeVazioError`, `LimiteInvalidoError` | Dev | ✅ Done |
| HU-02-T3 | Criar interface `CategoriaRepository` (ABC) | Dev | ✅ Done |
| HU-02-T4 | Implementar use case `CriarCategoria` | Dev | ✅ Done |
| HU-02-T5 | Implementar `CategoriaRepositorySQLite` | Dev | ✅ Done |
| HU-02-T6 | Criar rotas `POST /categorias` e `GET /categorias` | Dev | ✅ Done |
| HU-02-T7 | Escrever testes unitários (domínio + use case) | Dev | ✅ Done |

### Rastreabilidade

| Artefato | Arquivo |
|---|---|
| Entidade | `domain/entities/categoria.py` |
| Exceções | `domain/exceptions.py` |
| Interface | `use_cases/interfaces/categoria_repository.py` |
| Use Case | `use_cases/criar_categoria.py` |
| Repositório | `infra/repositories/categoria_repository_sqlite.py` |
| Rota | `app/routes/categoria_routes.py` |
| Testes domínio | `tests/domain/test_categoria.py` (7 testes) |
| Testes use case | `tests/use_cases/test_criar_categoria.py` (4 testes) |

---

## HU-03 — Consultar Saldo Atual

| Campo | Valor |
|---|---|
| **ID** | HU-03 |
| **Épico** | EP-03 — Relatórios Financeiros |
| **Feature** | FT-05 — Consulta de Saldo |
| **Story Points** | 3 |
| **Prioridade** | Must Have |
| **Sprint** | Sprint 1 |
| **Status** | ✅ Done |

### Narrativa

> **Como** usuário do FinTrack,
> **quero** consultar meu saldo financeiro atual,
> **para que** eu saiba quanto dinheiro tenho disponível (entradas − saídas).

### Critérios de Aceitação

- [x] CA-01: O saldo deve ser calculado como a soma de todas as entradas menos
  a soma de todas as saídas.
- [x] CA-02: Se não houver transações, o saldo deve ser 0.
- [x] CA-03: O saldo pode ser negativo (saídas > entradas).
- [x] CA-04: O endpoint `GET /saldo` deve retornar `{"saldo": "valor"}` com
  o saldo formatado como string decimal.
- [x] CA-05: A listagem de transações (`GET /transacoes`) deve estar disponível
  para complementar a consulta.

### Subtasks

| ID | Subtask | Responsável | Status |
|---|---|---|---|
| HU-03-T1 | Implementar método `valor_com_sinal()` na entidade Transacao | Dev | ✅ Done |
| HU-03-T2 | Implementar use case `CalcularSaldo` | Dev | ✅ Done |
| HU-03-T3 | Implementar use case `ListarTransacoes` | Dev | ✅ Done |
| HU-03-T4 | Criar rotas `GET /saldo` e `GET /transacoes` | Dev | ✅ Done |
| HU-03-T5 | Escrever testes unitários (use cases) | Dev | ✅ Done |

### Rastreabilidade

| Artefato | Arquivo |
|---|---|
| Método `valor_com_sinal` | `domain/entities/transacao.py` |
| Use Case (saldo) | `use_cases/calcular_saldo.py` |
| Use Case (listagem) | `use_cases/listar_transacoes.py` |
| Rota | `app/routes/transacao_routes.py` |
| Testes use case | `tests/use_cases/test_calcular_saldo.py` (4 testes) |
| Testes use case | `tests/use_cases/test_listar_transacoes.py` (3 testes) |

---

## HU-04 — Visualizar Totais por Categoria

| Campo | Valor |
|---|---|
| **ID** | HU-04 |
| **Épico** | EP-03 — Relatórios Financeiros |
| **Feature** | FT-06 — Relatório por Categoria |
| **Story Points** | 5 |
| **Prioridade** | Should Have |
| **Sprint** | Sprint 1 |
| **Status** | ✅ Done |

### Narrativa

> **Como** usuário do FinTrack,
> **quero** visualizar o total de movimentações agrupado por categoria,
> **para que** eu entenda como meu dinheiro está distribuído entre os diferentes
> tipos de gasto e receita.

### Critérios de Aceitação

- [x] CA-01: O relatório deve agrupar as transações por categoria.
- [x] CA-02: Cada categoria deve exibir o total líquido (entradas − saídas
  daquela categoria).
- [x] CA-03: Categorias sem transações não devem aparecer no relatório.
- [x] CA-04: O endpoint `GET /relatorios/por-categoria` deve retornar
  `{"categorias": [...]}` com id, nome e total de cada categoria.
- [x] CA-05: Os valores monetários devem ser retornados como strings decimais
  para preservar precisão.

### Subtasks

| ID | Subtask | Responsável | Status |
|---|---|---|---|
| HU-04-T1 | Criar dataclass `TotalCategoria` | Dev | ✅ Done |
| HU-04-T2 | Implementar use case `TotalPorCategoria` | Dev | ✅ Done |
| HU-04-T3 | Criar rota `GET /relatorios/por-categoria` | Dev | ✅ Done |
| HU-04-T4 | Escrever testes unitários | Dev | ✅ Done |

### Rastreabilidade

| Artefato | Arquivo |
|---|---|
| Dataclass | `use_cases/total_por_categoria.py` |
| Use Case | `use_cases/total_por_categoria.py` |
| Rota | `app/routes/transacao_routes.py` |
| Testes use case | `tests/use_cases/test_total_por_categoria.py` (4 testes) |
