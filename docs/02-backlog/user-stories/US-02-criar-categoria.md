# US-02 — Criar Categoria de Transação

## História

> **Como** João (universitário) ou Marina (freelancer),
> **quero** criar categorias para organizar minhas transações,
> **para** classificar entradas e saídas por tipo (Alimentação, Transporte,
> Salário, Cliente X) e ter relatórios agrupados.

## Metadados

| Campo | Valor |
|---|---|
| ID | US-02 |
| Épico pai | EPIC-01 |
| Feature pai | F-01 |
| Persona | João, Marina |
| Story Points | 3 |
| Prioridade | Alta |
| Status | Done |

## Descrição complementar

O usuário informa o nome da categoria e, opcionalmente, um limite mensal de
gastos. O sistema cria a categoria como objeto de domínio (validando nome e
limite) e a persiste via repositório. Um segundo endpoint permite listar todas
as categorias cadastradas. O limite mensal é armazenado mas não é verificado
automaticamente ao criar transações — serve como referência para o usuário.

## Regras de negócio

- **RN-02.1** — O nome da categoria não pode ser vazio nem conter apenas
  espaços em branco.
- **RN-02.2** — O limite mensal, se informado, deve ser ≥ 0.
- **RN-02.3** — O limite mensal é armazenado como `Decimal` para preservar
  precisão monetária. Valores numéricos são convertidos automaticamente.
- **RN-02.4** — O limite mensal não é verificado em tempo de transação
  (campo informativo; enforcement não implementado).

## Critérios de aceitação (BDD)

### CA-02.1 — Criação de categoria sem limite

> **Dado que** o usuário quer organizar transações em uma nova classificação,
> **quando** envia `POST /categorias` com nome "Alimentação" sem campo
> `limite_mensal`,
> **então** o sistema cria a categoria com id único, `limite_mensal` nulo,
> persiste no repositório e retorna status 201 com o JSON da categoria.

### CA-02.2 — Criação de categoria com limite mensal

> **Dado que** o usuário quer definir um teto de referência para gastos,
> **quando** envia `POST /categorias` com nome "Lazer" e `limite_mensal` 500,
> **então** o sistema cria a categoria com `limite_mensal` = Decimal("500"),
> persiste e retorna status 201.

### CA-02.3 — Rejeição por nome vazio

> **Dado que** o campo `nome` está vazio ou contém apenas espaços,
> **quando** o usuário envia `POST /categorias`,
> **então** o sistema retorna status 422 com a mensagem de erro
> `NomeVazioError` e a categoria não é persistida.

### CA-02.4 — Rejeição por limite negativo

> **Dado que** o usuário informa `limite_mensal` = −100,
> **quando** envia `POST /categorias`,
> **então** o sistema retorna status 422 com a mensagem de erro
> `LimiteInvalidoError`.

## Definition of Ready (verificado)

- [x] Narrativa no formato "Como / quero / para"
- [x] Persona declarada (João, Marina)
- [x] Critérios de aceitação escritos em formato BDD e testáveis
- [x] Story Points estimados (3)
- [x] Dependências mapeadas (nenhuma — esta história é pré-requisito de US-01)
- [x] Sem ambiguidade nos campos e validações

## Definition of Done

### Funcional
- [x] Endpoint `POST /categorias` cria categoria e retorna 201
- [x] Endpoint `GET /categorias` lista todas as categorias
- [x] Validações de domínio rejeitam nome vazio e limite negativo

### Qualidade de código
- [x] Código segue PEP-8 (verificado com `ruff check .`, zero erros)
- [x] Use case `CriarCategoria` depende apenas da ABC `CategoriaRepository`
- [x] Rota `POST /categorias` delega ao use case sem lógica de negócio
- [ ] Rota `GET /categorias` chama `categoria_repo.listar()` direto, sem use case (desvio documentado abaixo)

### NFR — Manutenibilidade
- [x] Entidade `Categoria` é objeto puro Python sem dependência de framework ou banco
- [x] Use case importa apenas ABC de `use_cases/interfaces/`, não `infra/`
- [x] Trocar SQLite por outro adapter não exige alterar `CriarCategoria`

### NFR — Testabilidade
- [x] Use case testado isoladamente com `FakeCategoriaRepository`
- [x] 4 testes no use case cobrindo happy path + exceções + persistência
- [x] 7 testes na entidade `Categoria` cobrindo criação válida e violações
- [x] Cobertura: `use_cases/criar_categoria.py` = 100% (11/11 statements)

## Nota de implementação

O endpoint `GET /categorias` (`categoria_routes.py:39-50`) chama
`categoria_repo.listar()` diretamente, sem intermediação de um use case
`ListarCategorias`. A operação é uma leitura simples sem lógica de negócio,
mas é um desvio da convenção de sempre intermediar via use case.

## Rastreabilidade (código que implementa esta história)

| Camada | Arquivo | Classe/Função |
|---|---|---|
| Entidade | `domain/entities/categoria.py` | `Categoria` |
| Exceções | `domain/exceptions.py` | `NomeVazioError`, `LimiteInvalidoError` |
| Interface | `use_cases/interfaces/categoria_repository.py` | `CategoriaRepository` |
| Use Case | `use_cases/criar_categoria.py` | `CriarCategoria.executar()` |
| Repositório | `infra/repositories/categoria_repository_sqlite.py` | `CategoriaRepositorySQLite` |
| Rota | `app/routes/categoria_routes.py` | `criar_categoria()`, `listar_categorias()` |
| Teste (domínio) | `tests/domain/test_categoria.py` | `TestCategoriaCriacaoValida`, `TestCategoriaRegraDeNegocio` |
| Teste (use case) | `tests/use_cases/test_criar_categoria.py` | `TestCriarCategoria` (4 testes) |
