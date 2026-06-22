# US-01 — Registrar Transação Financeira

## História

> **Como** João (universitário) ou Marina (freelancer),
> **quero** registrar uma transação financeira (entrada ou saída) vinculada a
> uma categoria,
> **para** manter um histórico das minhas movimentações e alimentar o cálculo
> de saldo e relatórios.

## Metadados

| Campo | Valor |
|---|---|
| ID | US-01 |
| Épico pai | EPIC-02 |
| Feature pai | F-02 |
| Persona | João, Marina |
| Story Points | 5 |
| Prioridade | Alta |
| Status | Done |

## Descrição complementar

O usuário informa descrição, valor monetário, tipo (ENTRADA ou SAIDA),
categoria e, opcionalmente, uma data. Se a data não for informada, o sistema
usa a data atual. A transação é criada como objeto de domínio (com validações)
e persistida via repositório. O endpoint retorna a transação criada em JSON.

## Regras de negócio

- **RN-01.1** — O valor deve ser estritamente positivo (> 0). O sinal é
  determinado pelo tipo, não pelo valor.
- **RN-01.2** — A descrição não pode ser vazia nem conter apenas espaços em
  branco.
- **RN-01.3** — O tipo deve ser ENTRADA ou SAIDA. Qualquer outro valor é
  rejeitado.
- **RN-01.4** — A categoria informada deve existir no repositório. Transações
  com `categoria_id` inexistente são rejeitadas.
- **RN-01.5** — Se a data não for informada, o sistema atribui `date.today()`.

## Critérios de aceitação (BDD)

### CA-01.1 — Registro de transação de entrada

> **Dado que** existe uma categoria "Salário" cadastrada no sistema,
> **quando** o usuário envia `POST /transacoes` com descrição "Salário mensal",
> valor 5000, tipo "ENTRADA" e `categoria_id` da categoria "Salário",
> **então** o sistema cria a transação com id único, tipo ENTRADA, valor 5000,
> persiste no repositório e retorna status 201 com o JSON da transação.

### CA-01.2 — Rejeição por categoria inexistente

> **Dado que** não existe nenhuma categoria com id "id-que-nao-existe",
> **quando** o usuário envia `POST /transacoes` referenciando esse
> `categoria_id`,
> **então** o sistema retorna status 404 com a mensagem de erro
> `CategoriaInexistenteError`.

### CA-01.3 — Rejeição por valor inválido

> **Dado que** existe uma categoria cadastrada,
> **quando** o usuário envia `POST /transacoes` com valor −50,
> **então** o sistema retorna status 422 com a mensagem de erro
> `ValorInvalidoError` e a transação não é persistida.

### CA-01.4 — Rejeição por descrição vazia

> **Dado que** existe uma categoria cadastrada,
> **quando** o usuário envia `POST /transacoes` com descrição "" (vazia),
> **então** o sistema retorna status 422 com a mensagem de erro
> `DescricaoVaziaError`.

### CA-01.5 — Data padrão quando não informada

> **Dado que** existe uma categoria cadastrada e o usuário não informa o campo
> `data`,
> **quando** o sistema cria a transação,
> **então** a data atribuída é `date.today()` do momento da criação.

## Definition of Ready (verificado)

- [x] Narrativa no formato "Como / quero / para"
- [x] Persona declarada (João, Marina)
- [x] Critérios de aceitação escritos em formato BDD e testáveis
- [x] Story Points estimados (5)
- [x] Dependências mapeadas (requer US-02 — categoria deve existir)
- [x] Sem ambiguidade nos campos e validações

## Definition of Done

### Funcional
- [x] Endpoint `POST /transacoes` cria transação e retorna 201
- [x] Endpoint `GET /transacoes` lista todas as transações
- [x] Validações de domínio rejeitam dados inválidos com exceções específicas
- [x] Transação persistida no banco via repositório

### Qualidade de código
- [x] Código segue PEP-8 (verificado com `ruff check .`, zero erros)
- [x] Use case `CriarTransacao` depende apenas de ABCs (`TransacaoRepository`, `CategoriaRepository`)
- [x] Rota Flask não contém lógica de negócio — delega ao use case

### NFR — Manutenibilidade
- [x] Entidade `Transacao` é objeto puro Python sem dependência de framework ou banco
- [x] Use case importa apenas ABCs de `use_cases/interfaces/`, não `infra/`
- [x] Trocar SQLite por outro adapter não exige alterar `CriarTransacao`

### NFR — Testabilidade
- [x] Use case testado isoladamente com `FakeTransacaoRepository` e `FakeCategoriaRepository`
- [x] 6 testes no use case cobrindo happy path + exceções
- [x] 11 testes na entidade `Transacao` cobrindo criação válida, `valor_com_sinal` e violações
- [x] Cobertura: `use_cases/criar_transacao.py` = 100% (21/21 statements)

## Rastreabilidade (código que implementa esta história)

| Camada | Arquivo | Classe/Função |
|---|---|---|
| Entidade | `domain/entities/transacao.py` | `Transacao`, `TipoTransacao` |
| Exceções | `domain/exceptions.py` | `ValorInvalidoError`, `DescricaoVaziaError`, `TipoInvalidoError`, `CategoriaInexistenteError` |
| Interface | `use_cases/interfaces/transacao_repository.py` | `TransacaoRepository` |
| Interface | `use_cases/interfaces/categoria_repository.py` | `CategoriaRepository` |
| Use Case | `use_cases/criar_transacao.py` | `CriarTransacao.executar()` |
| Use Case | `use_cases/listar_transacoes.py` | `ListarTransacoes.executar()` |
| Repositório | `infra/repositories/transacao_repository_sqlite.py` | `TransacaoRepositorySQLite` |
| Rota | `app/routes/transacao_routes.py` | `criar_transacao()`, `listar_transacoes()` |
| Teste (domínio) | `tests/domain/test_transacao.py` | `TestTransacaoCriacaoValida`, `TestTransacaoValorComSinal`, `TestTransacaoRegraDeNegocio` |
| Teste (use case) | `tests/use_cases/test_criar_transacao.py` | `TestCriarTransacao` (6 testes) |
| Teste (use case) | `tests/use_cases/test_listar_transacoes.py` | `TestListarTransacoes` (3 testes) |
