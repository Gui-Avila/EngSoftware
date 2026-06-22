# Matriz de Rastreabilidade — FinTrack

## História → Código → Teste

| História | Feature | Use Case(s) | Entidade(s) | Endpoint(s) | Arquivo(s) de Teste | Status |
|---|---|---|---|---|---|---|
| US-01 | F-02 | `CriarTransacao`, `ListarTransacoes` | `Transacao`, `TipoTransacao` | `POST /transacoes`, `GET /transacoes` | `test_criar_transacao.py` (6), `test_listar_transacoes.py` (3), `test_transacao.py` (11) | Done |
| US-02 | F-01 | `CriarCategoria` | `Categoria` | `POST /categorias`, `GET /categorias` | `test_criar_categoria.py` (4), `test_categoria.py` (7) | Done |
| US-03 | F-03 | `CalcularSaldo`, `ListarTransacoes` | `Transacao` | `GET /saldo`, `GET /transacoes` | `test_calcular_saldo.py` (4), `test_listar_transacoes.py` (3) | Done |
| US-04 | F-04 | `TotalPorCategoria` | `Transacao`, `Categoria`, `TotalCategoria` | `GET /relatorios/por-categoria` | `test_total_por_categoria.py` (4) | Done |

## Cobertura reversa (código → história)

Garante que todo use case tem justificativa de negócio — nenhum código órfão.

| Use Case | Arquivo | História(s) que o originou | Justificativa |
|---|---|---|---|
| `CriarTransacao` | `use_cases/criar_transacao.py` | US-01 | Registro de movimentação financeira |
| `CriarCategoria` | `use_cases/criar_categoria.py` | US-02 | Classificação de transações |
| `ListarTransacoes` | `use_cases/listar_transacoes.py` | US-01, US-03 | Visualização de histórico + composição do saldo |
| `CalcularSaldo` | `use_cases/calcular_saldo.py` | US-03 | Saldo atual do usuário |
| `TotalPorCategoria` | `use_cases/total_por_categoria.py` | US-04 | Distribuição de valores por categoria |

Todos os 5 use cases mapeiam para ao menos uma história. `ListarTransacoes`
serve duas histórias (US-01 para visualização de transações criadas e US-03
como complemento à consulta de saldo).

## Mapa de dependências entre histórias

| História | Depende de | Motivo |
|---|---|---|
| US-01 | US-02 | `CriarTransacao` valida que `categoria_id` existe via `CategoriaRepository.buscar_por_id()` |
| US-02 | — | Sem dependências — é pré-requisito das demais |
| US-03 | US-01 | `CalcularSaldo` opera sobre transações já registradas |
| US-04 | US-01, US-02 | `TotalPorCategoria` itera categorias e busca transações de cada uma |

## Entidades e seus campos

| Entidade | Arquivo | Campos | Validações |
|---|---|---|---|
| `Transacao` | `domain/entities/transacao.py` | `id`, `descricao`, `valor`, `tipo`, `data`, `categoria_id` | valor > 0, descrição não vazia, tipo ∈ {ENTRADA, SAIDA} |
| `Categoria` | `domain/entities/categoria.py` | `id`, `nome`, `limite_mensal` | nome não vazio, limite ≥ 0 (se informado) |
| `TipoTransacao` | `domain/entities/transacao.py` | Enum: ENTRADA, SAIDA | — |
| `TotalCategoria` | `use_cases/total_por_categoria.py` | `categoria_id`, `nome`, `total` | Dataclass de resultado (sem validação) |

## Interfaces (ABCs) e implementações

| Interface | Arquivo | Métodos | Implementação SQLite | Fake (teste) |
|---|---|---|---|---|
| `TransacaoRepository` | `use_cases/interfaces/transacao_repository.py` | `salvar`, `listar`, `listar_por_categoria` | `TransacaoRepositorySQLite` | `FakeTransacaoRepository` |
| `CategoriaRepository` | `use_cases/interfaces/categoria_repository.py` | `salvar`, `buscar_por_id`, `listar` | `CategoriaRepositorySQLite` | `FakeCategoriaRepository` |

## Cobertura de testes

| Módulo | Statements | Missed | Cobertura |
|---|---|---|---|
| `domain/entities/categoria.py` | 18 | 0 | 100% |
| `domain/entities/transacao.py` | 33 | 0 | 100% |
| `domain/exceptions.py` | 7 | 0 | 100% |
| `use_cases/criar_transacao.py` | 21 | 0 | 100% |
| `use_cases/criar_categoria.py` | 11 | 0 | 100% |
| `use_cases/listar_transacoes.py` | 7 | 0 | 100% |
| `use_cases/calcular_saldo.py` | 8 | 0 | 100% |
| `use_cases/total_por_categoria.py` | 21 | 0 | 100% |
| `use_cases/interfaces/*.py` | 18 | 0 | 100% |
| **Total** | **144** | **0** | **100%** |

Dados obtidos via `pytest --cov --cov-report=term-missing` (source:
`domain/`, `use_cases/`; threshold: 80%; configuração em `pyproject.toml`).

## Observação: desvio arquitetural

O endpoint `GET /categorias` em `app/routes/categoria_routes.py` (linhas
39–50) chama `categoria_repo.listar()` diretamente, sem intermediação de um
use case `ListarCategorias`. A operação é uma leitura simples (sem lógica de
negócio), mas foge da convenção de que toda operação passa por um use case.
As demais 5 operações seguem o fluxo completo rota → use case → repositório.
