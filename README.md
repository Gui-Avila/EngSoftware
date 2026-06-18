# FinTrack — Gerenciador Financeiro Pessoal

Trabalho A2 de Engenharia de Software (PUC-Rio, Prof. Marcos Kalinowski). Aplicação web em Flask com Clean Architecture, SOLID e testes unitários com pytest. Registra transações financeiras (entradas e saídas), organiza por categoria, calcula saldo e totaliza por categoria.

## Como rodar

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python run.py
```

O servidor sobe em `http://127.0.0.1:5000`.

### Exemplos curl

```bash
# Criar categoria
curl -X POST http://127.0.0.1:5000/categorias \
  -H "Content-Type: application/json" \
  -d '{"nome": "Alimentação", "limite_mensal": "1000"}'

# Listar categorias
curl http://127.0.0.1:5000/categorias

# Criar transação (use o id retornado na categoria)
curl -X POST http://127.0.0.1:5000/transacoes \
  -H "Content-Type: application/json" \
  -d '{"descricao": "Mercado", "valor": "250.00", "tipo": "SAIDA", "categoria_id": "<id-da-categoria>"}'

# Listar transações
curl http://127.0.0.1:5000/transacoes

# Consultar saldo
curl http://127.0.0.1:5000/saldo

# Total por categoria
curl http://127.0.0.1:5000/relatorios/por-categoria
```

## Como testar

```bash
pytest
pytest --cov
pytest --cov --cov-report=term-missing
```

## Lint

```bash
ruff check .
```

## Arquitetura — Clean Architecture

Estrutura baseada no modelo de Leonardo Giordani (*Clean Architectures in Python*), adotado no material da disciplina. Quatro camadas concêntricas, dependências apontam sempre para dentro.

```
    ┌──────────────────────────────────────────────┐
    │           4. External / Drivers              │
    │               infra/                         │
    │  ┌────────────────────────────────────────┐  │
    │  │      3. Gateways / Adapters            │  │
    │  │            app/                        │  │
    │  │  ┌──────────────────────────────────┐  │  │
    │  │  │       2. Use Cases               │  │  │
    │  │  │         use_cases/               │  │  │
    │  │  │  ┌────────────────────────────┐  │  │  │
    │  │  │  │      1. Entities           │  │  │  │
    │  │  │  │        domain/             │  │  │  │
    │  │  │  └────────────────────────────┘  │  │  │
    │  │  └──────────────────────────────────┘  │  │
    │  └────────────────────────────────────────┘  │
    └──────────────────────────────────────────────┘
```

**Golden rule:** *"Talk inward with simple structures, talk outwards through interfaces."* Camadas internas nunca importam camadas externas. A comunicação para fora passa por interfaces abstratas (ABCs).

| Camada | Pasta | O que contém |
|---|---|---|
| 1. Entities | `domain/` | Entidades `Transacao` e `Categoria`, enum `TipoTransacao`, exceções de domínio. Zero dependências externas. |
| 2. Use Cases | `use_cases/` | 5 casos de uso + ABCs dos repositórios em `interfaces/`. Dependem só de `domain/` e das ABCs. |
| 3. Gateways | `app/` | Rotas Flask (Blueprints), `create_app()` com wiring/injeção de dependências. |
| 4. External | `infra/` | SQLite (database.py) + repositórios concretos (Adapters). |

## SOLID

| Princípio | Onde está aplicado | Por quê |
|---|---|---|
| **SRP** | `domain/entities/transacao.py` | A entidade contém só regras de negócio. Persistência fica no repositório (separação entidade/DAO, como o exemplo Animal/AnimalDAO do material). |
| **OCP** | `use_cases/interfaces/` | Novos repositórios (ex.: PostgreSQL) entram implementando a ABC, sem alterar os use cases existentes. |
| **LSP** | `infra/repositories/` e `tests/use_cases/conftest.py` | Tanto o repo SQLite quanto o fake in-memory implementam a mesma ABC e são intercambiáveis — o use case roda igual com qualquer um. |
| **ISP** | `use_cases/interfaces/transacao_repository.py` | Interfaces enxutas com só os métodos que os use cases precisam (`salvar`, `listar`, `listar_por_categoria`). Sem CRUD genérico inflado. |
| **DIP** | `use_cases/criar_transacao.py`, `app/main.py` | Use cases recebem ABCs por injeção no construtor. A implementação concreta (SQLite) é injetada só no wiring em `create_app()`. |

## Histórias de Usuário

| HU | Descrição | Use Case |
|---|---|---|
| HU-01 | Como usuário, quero registrar uma transação (entrada ou saída) para acompanhar minhas finanças. | `CriarTransacao` |
| HU-02 | Como usuário, quero criar categorias para organizar minhas transações. | `CriarCategoria` |
| HU-03 | Como usuário, quero consultar meu saldo atual (entradas menos saídas) para saber quanto tenho. | `CalcularSaldo`, `ListarTransacoes` |
| HU-04 | Como usuário, quero ver o total por categoria para entender onde gasto mais. | `TotalPorCategoria` |

## Endpoints

| Método | Rota | Use Case | Sucesso | Erro |
|---|---|---|---|---|
| POST | `/categorias` | CriarCategoria | 201 | 422 |
| GET | `/categorias` | — (repo direto) | 200 | — |
| POST | `/transacoes` | CriarTransacao | 201 | 404/422 |
| GET | `/transacoes` | ListarTransacoes | 200 | — |
| GET | `/saldo` | CalcularSaldo | 200 | — |
| GET | `/relatorios/por-categoria` | TotalPorCategoria | 200 | — |

## Critérios de Avaliação

| Critério (peso) | Como é atendido |
|---|---|
| App funcional, ≥3 use cases, ≥2 entidades (4,0) | 5 use cases, 2 entidades, 6 endpoints REST funcionais |
| Clean Architecture correta (2,0) | 4 camadas em pastas separadas; dependências apontam só para dentro; golden rule respeitada |
| SOLID correto (2,0) | SRP/OCP/LSP/ISP/DIP aplicados e comentados; tabela acima com arquivo de cada um |
| Testes unitários dos use cases (1,0) | 39 testes, use cases testados com fakes in-memory, isolados de Flask/SQLite, 100% de cobertura em domain/ e use_cases/ |
| PEP-8 (1,0) | ruff configurado e sem warnings; instrução de lint acima |

## Estrutura de pastas

```
├── run.py
├── domain/                          # Camada 1 — Entities
│   ├── entities/
│   │   ├── transacao.py
│   │   └── categoria.py
│   └── exceptions.py
├── use_cases/                       # Camada 2 — Use Cases
│   ├── interfaces/
│   │   ├── transacao_repository.py
│   │   └── categoria_repository.py
│   ├── criar_transacao.py
│   ├── criar_categoria.py
│   ├── listar_transacoes.py
│   ├── calcular_saldo.py
│   └── total_por_categoria.py
├── infra/                           # Camada 4 — External / Drivers
│   ├── db/
│   │   └── database.py
│   └── repositories/
│       ├── transacao_repository_sqlite.py
│       └── categoria_repository_sqlite.py
├── app/                             # Camada 3 — Gateways / Adapters
│   ├── main.py
│   └── routes/
│       ├── transacao_routes.py
│       └── categoria_routes.py
└── tests/
    ├── domain/
    │   ├── test_transacao.py
    │   └── test_categoria.py
    └── use_cases/
        ├── conftest.py
        ├── test_criar_transacao.py
        ├── test_criar_categoria.py
        ├── test_listar_transacoes.py
        ├── test_calcular_saldo.py
        └── test_total_por_categoria.py
```
