# US-04 — Visualizar Totais por Categoria

## História

> **Como** Marina (freelancer),
> **quero** visualizar o total de movimentações agrupado por categoria,
> **para** entender como meu dinheiro está distribuído entre tipos de despesa
> e fontes de receita.

## Metadados

| Campo | Valor |
|---|---|
| ID | US-04 |
| Épico pai | EPIC-03 |
| Feature pai | F-04 |
| Persona | Marina |
| Story Points | 5 |
| Prioridade | Média |
| Status | Done |

## Descrição complementar

O use case `TotalPorCategoria` itera todas as categorias, e para cada uma
busca as transações associadas e soma `valor_com_sinal()`. O resultado é uma
lista de `TotalCategoria` (dataclass com `categoria_id`, `nome`, `total`).
Categorias sem transações aparecem com total zero. O endpoint retorna o
relatório em JSON com valores monetários como strings.

## Regras de negócio

- **RN-04.1** — O total de cada categoria é a soma de `valor_com_sinal()`
  das suas transações (entradas positivas, saídas negativas).
- **RN-04.2** — Categorias cadastradas mas sem transações aparecem no
  relatório com total = 0.
- **RN-04.3** — Uma mesma categoria pode ter entradas e saídas; o total é
  o valor líquido.
- **RN-04.4** — Valores retornados como strings decimais para preservar
  precisão.

## Critérios de aceitação (BDD)

### CA-04.1 — Agrupamento correto por categoria

> **Dado que** existem as categorias "Alimentação" (com saídas de 200 e 80) e
> "Transporte" (com saída de 50),
> **quando** o usuário consulta `GET /relatorios/por-categoria`,
> **então** o sistema retorna `[{"nome": "Alimentação", "total": "-280"},
> {"nome": "Transporte", "total": "-50"}]`.

### CA-04.2 — Categoria sem transações retorna zero

> **Dado que** existe a categoria "Reserva" sem nenhuma transação vinculada,
> **quando** o usuário consulta `GET /relatorios/por-categoria`,
> **então** "Reserva" aparece no relatório com `total` = "0".

### CA-04.3 — Entradas e saídas na mesma categoria

> **Dado que** a categoria "Freelance" tem uma entrada de 1000 e uma saída de
> 300,
> **quando** o usuário consulta `GET /relatorios/por-categoria`,
> **então** "Freelance" aparece com `total` = "700".

### CA-04.4 — Sem categorias retorna lista vazia

> **Dado que** não existem categorias cadastradas,
> **quando** o usuário consulta `GET /relatorios/por-categoria`,
> **então** o sistema retorna `{"categorias": []}`.

## Definition of Ready (verificado)

- [x] Narrativa no formato "Como / quero / para"
- [x] Persona declarada (Marina)
- [x] Critérios de aceitação escritos em formato BDD e testáveis
- [x] Story Points estimados (5)
- [x] Dependências mapeadas (requer US-01 e US-02 — transações e categorias devem existir)
- [x] Sem ambiguidade na agregação (soma algébrica por categoria)

## Definition of Done

### Funcional
- [x] Endpoint `GET /relatorios/por-categoria` retorna totais por categoria
- [x] Categorias sem transações incluídas com total zero
- [x] Valores monetários serializados como string

### Qualidade de código
- [x] Código segue PEP-8 (verificado com `ruff check .`, zero erros)
- [x] `TotalPorCategoria` depende apenas das ABCs `TransacaoRepository` e `CategoriaRepository`
- [x] Rota Flask não contém lógica de agregação — delega ao use case

### NFR — Manutenibilidade
- [x] `TotalCategoria` é dataclass pura de resultado, sem acoplamento a framework
- [x] Use case importa apenas ABCs de `use_cases/interfaces/`
- [x] Lógica de agregação encapsulada no use case, fora da rota e do repositório

### NFR — Testabilidade
- [x] Use case testado com 4 cenários (vazio, sem transações, agrupamento, misto)
- [x] Testes usam `FakeTransacaoRepository` e `FakeCategoriaRepository` sem banco
- [x] Cobertura: `use_cases/total_por_categoria.py` = 100% (21/21 statements)

## Rastreabilidade (código que implementa esta história)

| Camada | Arquivo | Classe/Função |
|---|---|---|
| Entidade | `domain/entities/transacao.py` | `Transacao.valor_com_sinal()` |
| Entidade | `domain/entities/categoria.py` | `Categoria` |
| Resultado | `use_cases/total_por_categoria.py` | `TotalCategoria` (dataclass) |
| Use Case | `use_cases/total_por_categoria.py` | `TotalPorCategoria.executar()` |
| Interface | `use_cases/interfaces/transacao_repository.py` | `TransacaoRepository.listar_por_categoria()` |
| Interface | `use_cases/interfaces/categoria_repository.py` | `CategoriaRepository.listar()` |
| Repositório | `infra/repositories/transacao_repository_sqlite.py` | `TransacaoRepositorySQLite.listar_por_categoria()` |
| Rota | `app/routes/transacao_routes.py` | `total_por_categoria()` |
| Teste (use case) | `tests/use_cases/test_total_por_categoria.py` | `TestTotalPorCategoria` (4 testes) |
