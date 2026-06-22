# US-03 — Consultar Saldo Atual

## História

> **Como** João (universitário),
> **quero** consultar meu saldo financeiro atual,
> **para** saber quanto dinheiro tenho disponível antes de decidir novos
> gastos.

## Metadados

| Campo | Valor |
|---|---|
| ID | US-03 |
| Épico pai | EPIC-03 |
| Feature pai | F-03 |
| Persona | João |
| Story Points | 3 |
| Prioridade | Alta |
| Status | Done |

## Descrição complementar

O saldo é calculado como a soma algébrica de todas as transações: entradas
contribuem com +valor, saídas com −valor. O use case `CalcularSaldo` itera
todas as transações e acumula `valor_com_sinal()`. O use case
`ListarTransacoes` complementa, permitindo ao usuário ver o detalhamento que
compõe o saldo. O endpoint retorna o saldo como string decimal para preservar
precisão.

## Regras de negócio

- **RN-03.1** — Saldo = Σ `valor_com_sinal()` de todas as transações.
- **RN-03.2** — Sem transações, o saldo é 0 (zero).
- **RN-03.3** — O saldo pode ser negativo (saídas maiores que entradas).
- **RN-03.4** — O cálculo usa `Decimal` para evitar erros de ponto flutuante.

## Critérios de aceitação (BDD)

### CA-03.1 — Saldo com entradas e saídas

> **Dado que** existem três transações: Salário +5000, Aluguel −1500,
> Mercado −500,
> **quando** o usuário consulta `GET /saldo`,
> **então** o sistema retorna `{"saldo": "3000"}`.

### CA-03.2 — Saldo zero sem transações

> **Dado que** não existem transações cadastradas,
> **quando** o usuário consulta `GET /saldo`,
> **então** o sistema retorna `{"saldo": "0"}`.

### CA-03.3 — Saldo negativo

> **Dado que** existe uma entrada de 100 e uma saída de 500,
> **quando** o usuário consulta `GET /saldo`,
> **então** o sistema retorna `{"saldo": "-400"}`.

### CA-03.4 — Listagem de transações retorna cópia independente

> **Dado que** existem transações cadastradas,
> **quando** o usuário consulta `GET /transacoes` e recebe a lista,
> **então** modificar a lista retornada não altera a coleção interna do
> repositório (o retorno é uma cópia).

## Definition of Ready (verificado)

- [x] Narrativa no formato "Como / quero / para"
- [x] Persona declarada (João)
- [x] Critérios de aceitação escritos em formato BDD e testáveis
- [x] Story Points estimados (3)
- [x] Dependências mapeadas (requer US-01 — transações devem existir para o saldo ter sentido)
- [x] Sem ambiguidade no cálculo (soma algébrica com sinal)

## Definition of Done

### Funcional
- [x] Endpoint `GET /saldo` retorna `{"saldo": "<valor>"}` corretamente
- [x] Endpoint `GET /transacoes` lista todas as transações
- [x] Saldo calculado como soma de `valor_com_sinal()` de todas as transações

### Qualidade de código
- [x] Código segue PEP-8 (verificado com `ruff check .`, zero erros)
- [x] `CalcularSaldo` e `ListarTransacoes` dependem apenas da ABC `TransacaoRepository`
- [x] Rotas Flask não contêm lógica de cálculo — delegam aos use cases

### NFR — Manutenibilidade
- [x] Use cases são classes com método único `executar()`, sem estado mutável
- [x] Nenhuma dependência de `infra/` nos use cases
- [x] `Transacao.valor_com_sinal()` encapsula a lógica de sinal na entidade

### NFR — Testabilidade
- [x] `CalcularSaldo` testado com 4 cenários (zero, misto, negativo, só entradas)
- [x] `ListarTransacoes` testado com 3 cenários (vazia, populada, cópia)
- [x] Todos os testes usam `FakeTransacaoRepository` sem tocar banco
- [x] Cobertura: `use_cases/calcular_saldo.py` = 100% (8/8), `use_cases/listar_transacoes.py` = 100% (7/7)

## Rastreabilidade (código que implementa esta história)

| Camada | Arquivo | Classe/Função |
|---|---|---|
| Entidade | `domain/entities/transacao.py` | `Transacao.valor_com_sinal()` |
| Use Case | `use_cases/calcular_saldo.py` | `CalcularSaldo.executar()` |
| Use Case | `use_cases/listar_transacoes.py` | `ListarTransacoes.executar()` |
| Rota | `app/routes/transacao_routes.py` | `consultar_saldo()`, `listar_transacoes()` |
| Teste (use case) | `tests/use_cases/test_calcular_saldo.py` | `TestCalcularSaldo` (4 testes) |
| Teste (use case) | `tests/use_cases/test_listar_transacoes.py` | `TestListarTransacoes` (3 testes) |
