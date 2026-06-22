# FinTrack — Gerenciador Financeiro Pessoal

Trabalho A2 de Engenharia de Software (PUC-Rio, Prof. Marcos Kalinowski). Aplicação web em Flask com Clean Architecture, SOLID e testes unitários com pytest.

O FinTrack permite registrar transações financeiras (entradas e saídas), organizá-las por categoria, consultar o saldo atual e ver o total gasto/recebido por categoria. Persistência em SQLite, API REST com JSON e interface web com dashboard.

---

## Sumário

- [Como rodar](#como-rodar)
- [Como testar](#como-testar)
- [Lint (PEP-8)](#lint-pep-8)
- [Estrutura de pastas](#estrutura-de-pastas)
- [Clean Architecture — mapa detalhado](#clean-architecture--mapa-detalhado)
  - [Camada 1: Entities (domain/)](#camada-1-entities--domain)
  - [Camada 2: Use Cases (use_cases/)](#camada-2-use-cases--use_cases)
  - [Camada 3: Interface Adapters (app/)](#camada-3-interface-adapters--app)
  - [Camada 4: Frameworks & Drivers (infra/)](#camada-4-frameworks--drivers--infra)
  - [Regra de ouro e fluxo de dependências](#regra-de-ouro-e-fluxo-de-dependências)
- [SOLID — onde e por quê](#solid--onde-e-por-quê)
  - [SRP — Responsabilidade Única](#srp--responsabilidade-única)
  - [OCP — Aberto/Fechado](#ocp--abertofechado)
  - [LSP — Substituição de Liskov](#lsp--substituição-de-liskov)
  - [ISP — Segregação de Interface](#isp--segregação-de-interface)
  - [DIP — Inversão de Dependência](#dip--inversão-de-dependência)
- [Padrão Adapter (GoF)](#padrão-adapter-gof)
- [Entidades de domínio](#entidades-de-domínio)
- [Casos de uso](#casos-de-uso)
- [Histórias de usuário](#histórias-de-usuário)
- [Endpoints da API REST](#endpoints-da-api-rest)
- [Frontend web](#frontend-web)
- [Testes unitários](#testes-unitários)
- [Cobertura de testes](#cobertura-de-testes)
- [Decisões técnicas](#decisões-técnicas)
- [Critérios de avaliação — mapeamento](#critérios-de-avaliação--mapeamento)

---

## Como rodar

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python run.py
```

O servidor sobe em `http://127.0.0.1:5000`. A interface web fica na raiz (`/`), a API REST nos endpoints abaixo.

### Exemplos curl

```bash
# Criar categoria
curl -X POST http://127.0.0.1:5000/categorias \
  -H "Content-Type: application/json" \
  -d '{"nome": "Alimentação", "limite_mensal": "1000"}'

# Listar categorias
curl http://127.0.0.1:5000/categorias

# Criar transação (substituir <id> pelo id retornado acima)
curl -X POST http://127.0.0.1:5000/transacoes \
  -H "Content-Type: application/json" \
  -d '{"descricao": "Mercado", "valor": "250.00", "tipo": "SAIDA", "categoria_id": "<id>"}'

# Listar transações
curl http://127.0.0.1:5000/transacoes

# Consultar saldo
curl http://127.0.0.1:5000/saldo

# Total por categoria
curl http://127.0.0.1:5000/relatorios/por-categoria
```

## Como testar

```bash
pytest                              # roda os 39 testes
pytest -v                           # verbose, mostra cada teste
pytest --cov                        # com cobertura
pytest --cov --cov-report=term-missing  # cobertura + linhas não cobertas
```

## Lint (PEP-8)

```bash
ruff check .
```

Configurado no `pyproject.toml` com regras E, F, W, I (isort) e N (naming). Line-length 99, target Python 3.12. Zero warnings no estado atual.

---

## Estrutura de pastas

```
fintrack/
├── run.py                                  # Entrypoint
├── requirements.txt                        # flask, pytest, pytest-cov, ruff
├── pyproject.toml                          # Configuração pytest + cov + ruff
├── .gitignore
│
├── domain/                                 # CAMADA 1 — Entities
│   ├── entities/
│   │   ├── transacao.py                    #   Transacao + TipoTransacao(Enum)
│   │   └── categoria.py                   #   Categoria
│   └── exceptions.py                      #   Exceções de domínio
│
├── use_cases/                              # CAMADA 2 — Use Cases
│   ├── interfaces/                         #   ABCs dos repositórios (DIP + ISP)
│   │   ├── transacao_repository.py
│   │   └── categoria_repository.py
│   ├── criar_transacao.py                  #   HU-01
│   ├── criar_categoria.py                 #   HU-02
│   ├── listar_transacoes.py               #   HU-01/HU-03
│   ├── calcular_saldo.py                  #   HU-03
│   └── total_por_categoria.py             #   HU-04
│
├── infra/                                  # CAMADA 4 — Frameworks & Drivers
│   ├── db/
│   │   └── database.py                    #   Conexão SQLite + DDL
│   └── repositories/                      #   Adapters concretos
│       ├── transacao_repository_sqlite.py
│       └── categoria_repository_sqlite.py
│
├── app/                                    # CAMADA 3 — Interface Adapters
│   ├── main.py                            #   Factory create_app() + wiring
│   ├── routes/
│   │   ├── categoria_routes.py            #   Blueprint JSON
│   │   ├── transacao_routes.py            #   Blueprint JSON
│   │   └── frontend_routes.py             #   Blueprint HTML
│   ├── templates/                         #   Jinja2 templates
│   │   ├── base.html
│   │   ├── index.html                     #   Dashboard
│   │   ├── categorias.html
│   │   └── transacoes.html
│   └── static/
│       ├── css/style.css
│       └── js/app.js
│
└── tests/
    ├── domain/
    │   ├── test_transacao.py               # 11 testes
    │   └── test_categoria.py              # 7 testes
    └── use_cases/
        ├── conftest.py                    # Fakes in-memory (fixtures)
        ├── test_criar_transacao.py        # 6 testes
        ├── test_criar_categoria.py        # 4 testes
        ├── test_listar_transacoes.py      # 3 testes
        ├── test_calcular_saldo.py         # 4 testes
        └── test_total_por_categoria.py    # 4 testes
```

---

## Clean Architecture — mapa detalhado

Modelo de Leonardo Giordani (*Clean Architectures in Python*), adotado no material do professor. Quatro camadas concêntricas; dependências apontam sempre para dentro.

```
    ┌──────────────────────────────────────────────┐
    │        4. Frameworks & Drivers               │
    │              infra/                          │
    │  ┌────────────────────────────────────────┐  │
    │  │     3. Interface Adapters              │  │
    │  │           app/                         │  │
    │  │  ┌──────────────────────────────────┐  │  │
    │  │  │      2. Use Cases                │  │  │
    │  │  │        use_cases/                │  │  │
    │  │  │  ┌────────────────────────────┐  │  │  │
    │  │  │  │     1. Entities            │  │  │  │
    │  │  │  │       domain/              │  │  │  │
    │  │  │  └────────────────────────────┘  │  │  │
    │  │  └──────────────────────────────────┘  │  │
    │  └────────────────────────────────────────┘  │
    └──────────────────────────────────────────────┘
```

### Camada 1: Entities (`domain/`)

O núcleo. Contém as entidades `Transacao` e `Categoria`, o enum `TipoTransacao` e as exceções de domínio. Aqui ficam todas as regras de negócio: valor positivo, descrição não vazia, tipo válido, nome não vazio, limite >= 0.

**Zero dependências externas.** Nenhum `import` de Flask, sqlite3 ou qualquer lib de infraestrutura. Usa apenas a stdlib do Python (`dataclasses`, `decimal`, `enum`, `uuid`, `datetime`). Isso garante que o domínio é puro e testável sem nenhum setup.

**Arquivos:**
- `domain/entities/transacao.py` — dataclass `Transacao` com `__post_init__` que valida as regras e converte tipos. Método de domínio `valor_com_sinal()` retorna `+valor` para ENTRADA e `-valor` para SAIDA (usado pelo `CalcularSaldo` e `TotalPorCategoria`).
- `domain/entities/categoria.py` — dataclass `Categoria` com validação de nome e limite.
- `domain/exceptions.py` — hierarquia de exceções de domínio (`DominioError` como base, subclasses para cada violação). Fazem parte do vocabulário do negócio, não de infraestrutura.

### Camada 2: Use Cases (`use_cases/`)

Regras de negócio da aplicação. Cada use case é uma classe com um método `executar(...)`. Orquestram as entidades e dependem apenas de:
- `domain/` (entidades e exceções)
- ABCs em `use_cases/interfaces/` (contratos de repositório)

Nunca importam implementações concretas (SQLite, Flask). Isso é DIP na prática.

**Arquivos:**
- `use_cases/interfaces/transacao_repository.py` — ABC `TransacaoRepository` com `salvar()`, `listar()`, `listar_por_categoria()`.
- `use_cases/interfaces/categoria_repository.py` — ABC `CategoriaRepository` com `salvar()`, `buscar_por_id()`, `listar()`.
- `use_cases/criar_transacao.py` — valida que a categoria existe (via ABC), cria a entidade `Transacao` (regras validam no construtor), persiste via repositório.
- `use_cases/criar_categoria.py` — cria a entidade `Categoria` e persiste.
- `use_cases/listar_transacoes.py` — delega para `repo.listar()`.
- `use_cases/calcular_saldo.py` — soma `valor_com_sinal()` de todas as transações.
- `use_cases/total_por_categoria.py` — para cada categoria, busca suas transações e soma `valor_com_sinal()`. Retorna lista de `TotalCategoria` (dataclass de resultado).

### Camada 3: Interface Adapters (`app/`)

Converte entre o mundo externo (HTTP, HTML) e os use cases. Não contém regra de negócio.

**Arquivos:**
- `app/main.py` — `create_app()`: factory Flask que faz o **wiring**. Instancia os repositórios concretos (SQLite), injeta nos use cases via construtor, registra os Blueprints. Este é o único ponto do sistema que conhece tanto as abstrações (ABCs) quanto as implementações concretas. Aqui a inversão de dependência é "amarrada".
- `app/routes/categoria_routes.py` — Blueprint JSON. `POST /categorias` converte JSON para chamada de use case, devolve 201. `GET /categorias` lista direto do repositório. Erros de domínio viram 422.
- `app/routes/transacao_routes.py` — Blueprint JSON. `POST /transacoes` (201), `GET /transacoes` (200), `GET /saldo` (200), `GET /relatorios/por-categoria` (200). `CategoriaInexistenteError` vira 404, demais erros de domínio viram 422.
- `app/routes/frontend_routes.py` — Blueprint HTML. Renderiza templates Jinja2 para dashboard (`/`), categorias (`/ui/categorias`) e transações (`/ui/transacoes`). Mesma camada que as rotas JSON — é outro adapter de entrega.
- `app/templates/` — templates Jinja2 com JS que consome a API REST via `fetch()`.
- `app/static/` — CSS (tema escuro, responsivo) e JS utilitário.

### Camada 4: Frameworks & Drivers (`infra/`)

Tecnologias externas: SQLite, conexão, DDL. Nenhuma regra de negócio.

**Arquivos:**
- `infra/db/database.py` — `init_db()` cria as tabelas `categorias` e `transacoes`. `get_connection()` retorna conexão SQLite com `row_factory` e foreign keys habilitadas.
- `infra/repositories/categoria_repository_sqlite.py` — implementação concreta de `CategoriaRepository` usando sqlite3. Adapter (GoF): adapta SQLite à interface que o domínio espera.
- `infra/repositories/transacao_repository_sqlite.py` — implementação concreta de `TransacaoRepository` usando sqlite3. Adapter (GoF).

### Regra de ouro e fluxo de dependências

> *"Talk inward with simple structures, talk outwards through interfaces."*

- **Para dentro:** as camadas externas passam dados simples (strings, Decimal, dicts, dataclasses) para as camadas internas. As rotas Flask recebem JSON, extraem os campos, e chamam `use_case.executar()` com parâmetros primitivos.
- **Para fora:** as camadas internas se comunicam com o mundo externo através de interfaces abstratas (ABCs). Os use cases chamam `self._repo.salvar(transacao)` sem saber se `_repo` é SQLite, PostgreSQL ou um fake em memória.
- **Dependências:** `domain/` não importa nada externo. `use_cases/` importa `domain/` e suas próprias ABCs. `infra/` importa `domain/` e as ABCs. `app/` importa tudo (no wiring) e as exceções de domínio (nas rotas). As setas apontam sempre para dentro.

Fluxo concreto de uma requisição `POST /transacoes`:

```
HTTP Request (JSON)
    → app/routes/transacao_routes.py     [extrai campos do JSON]
    → use_cases/criar_transacao.py       [valida categoria via ABC, cria entidade]
    → domain/entities/transacao.py       [valida regras no __post_init__]
    → use_cases/interfaces/ (ABC)        [repo.salvar() — interface abstrata]
    → infra/repositories/ (SQLite)       [INSERT no banco — implementação concreta]
    ← HTTP Response 201 (JSON)
```

---

## SOLID — onde e por quê

### SRP — Responsabilidade Única

> *Uma classe não deve ter mais de um motivo para mudar.*

| Arquivo | Aplicação |
|---|---|
| `domain/entities/transacao.py` | A entidade `Transacao` contém apenas regras de negócio (valor > 0, tipo válido, descrição não vazia, `valor_com_sinal()`). Ela não sabe se salvar, não sabe nada de banco, não sabe nada de HTTP. Se as regras de validação mudarem, muda este arquivo. Se a persistência mudar, muda o repositório. São motivos de mudança separados — exatamente o exemplo Animal/AnimalDAO do material. |
| `domain/entities/categoria.py` | Mesma lógica: só regras de negócio (nome não vazio, limite >= 0). |
| `use_cases/criar_transacao.py` | Orquestra a criação: verifica categoria, cria entidade, persiste. Não valida regras de negócio (a entidade faz isso) e não sabe como persistir (o repositório faz isso). |
| `app/routes/transacao_routes.py` | Só converte HTTP (JSON) para chamada de use case e use case para resposta HTTP. Não contém regra de negócio nem lógica de persistência. |
| `infra/repositories/transacao_repository_sqlite.py` | Só persiste e reconstitui objetos via SQLite. Não valida nada. |

Cada classe tem um único motivo para mudar: a entidade muda se as regras mudarem, o repositório muda se o banco mudar, a rota muda se o contrato HTTP mudar.

### OCP — Aberto/Fechado

> *Aberto para extensão, fechado para modificação.*

| Arquivo | Aplicação |
|---|---|
| `use_cases/interfaces/transacao_repository.py` | A ABC `TransacaoRepository` define o contrato. Para adicionar um repositório PostgreSQL, basta criar uma nova classe que herda da ABC e implementa os métodos. Nenhum use case precisa ser modificado — só o wiring em `app/main.py` muda para instanciar o novo repositório. |
| `use_cases/interfaces/categoria_repository.py` | Mesma lógica. O sistema é extensível por novas implementações, sem tocar no código existente dos use cases. |
| `domain/entities/transacao.py` | O enum `TipoTransacao` pode ser estendido (ex.: TRANSFERENCIA) sem modificar a estrutura da classe — basta adicionar o novo valor e tratar no `valor_com_sinal()`. |

Exemplo concreto: se amanhã quisermos trocar SQLite por PostgreSQL, criamos `infra/repositories/transacao_repository_postgres.py` implementando a mesma ABC, e em `app/main.py` trocamos a instanciação. Os 5 use cases e os 39 testes continuam funcionando sem alteração.

### LSP — Substituição de Liskov

> *Uma subclasse deve poder substituir sua superclasse sem quebrar o programa.*

| Arquivo | Aplicação |
|---|---|
| `infra/repositories/transacao_repository_sqlite.py` | Implementa `TransacaoRepository` (ABC). Pode substituir qualquer outra implementação sem que o use case perceba. |
| `infra/repositories/categoria_repository_sqlite.py` | Implementa `CategoriaRepository` (ABC). Mesma garantia. |
| `tests/use_cases/conftest.py` | `FakeTransacaoRepository` e `FakeCategoriaRepository` implementam as mesmas ABCs com `list`/`dict` em memória. **Esta é a prova concreta de LSP:** os mesmos use cases rodam nos testes com fakes e em produção com SQLite, sem mudar uma linha. O comportamento é intercambiável. |

O LSP é verificável olhando os testes: os 21 testes de use case usam os fakes, e a aplicação real usa os repos SQLite. Mesma interface, mesmos contratos, comportamento substituível.

### ISP — Segregação de Interface

> *Várias interfaces específicas são melhores que uma genérica.*

| Arquivo | Aplicação |
|---|---|
| `use_cases/interfaces/transacao_repository.py` | Interface enxuta: `salvar()`, `listar()`, `listar_por_categoria()`. Só o que os use cases precisam. Não tem `deletar()`, `atualizar()`, `buscar_por_id()` — nenhum use case pede isso. Se houvesse um CRUD genérico com 10 métodos, os clients teriam que implementar coisas que não usam. |
| `use_cases/interfaces/categoria_repository.py` | Interface enxuta: `salvar()`, `buscar_por_id()`, `listar()`. O `buscar_por_id()` existe porque `CriarTransacao` precisa validar que a categoria existe. |

As duas interfaces são separadas (uma para transações, outra para categorias) em vez de uma interface genérica "Repository" que misturaria os dois domínios. Cada use case depende apenas da interface que usa.

### DIP — Inversão de Dependência

> *Depender de abstrações, não de implementações.*

| Arquivo | Aplicação |
|---|---|
| `use_cases/criar_transacao.py` | O construtor recebe `TransacaoRepository` e `CategoriaRepository` (ABCs). Nunca faz `import` de `TransacaoRepositorySQLite`. Não sabe que SQLite existe. |
| `use_cases/criar_categoria.py` | Construtor recebe `CategoriaRepository` (ABC). |
| `use_cases/calcular_saldo.py` | Construtor recebe `TransacaoRepository` (ABC). |
| `use_cases/listar_transacoes.py` | Construtor recebe `TransacaoRepository` (ABC). |
| `use_cases/total_por_categoria.py` | Construtor recebe ambas ABCs. |
| `app/main.py` | **Ponto de wiring.** Único lugar que importa tanto as ABCs quanto as implementações concretas. Instancia `CategoriaRepositorySQLite(conn)` e `TransacaoRepositorySQLite(conn)`, e passa para os construtores dos use cases. A inversão é "amarrada" aqui. |

Fluxo de dependência sem DIP (errado):
```
Use Case → SQLite Repository (acoplamento direto)
```

Fluxo de dependência com DIP (como implementamos):
```
Use Case → ABC (abstração)    ← SQLite Repository implementa
                              ← Fake Repository implementa (testes)
```

O módulo de alto nível (use case) não depende do módulo de baixo nível (SQLite). Ambos dependem da abstração (ABC).

---

## Padrão Adapter (GoF)

Os repositórios concretos em `infra/repositories/` são Adapters do padrão GoF. Eles adaptam a tecnologia externa (SQLite) à interface que o domínio espera (ABCs em `use_cases/interfaces/`).

- **Target (interface esperada):** `TransacaoRepository`, `CategoriaRepository` (ABCs).
- **Adaptee (tecnologia adaptada):** sqlite3 (`Connection`, `Cursor`, SQL).
- **Adapter:** `TransacaoRepositorySQLite`, `CategoriaRepositorySQLite`.

Exemplo em `transacao_repository_sqlite.py`: o método `salvar()` recebe uma entidade `Transacao` (domínio) e a converte em uma query SQL INSERT. O método `listar()` executa um SELECT e reconstitui entidades `Transacao` a partir das rows. A conversão entre o formato do domínio e o formato do banco é responsabilidade exclusiva do Adapter.

---

## Entidades de domínio

### Transacao

| Campo | Tipo | Regra |
|---|---|---|
| `id` | `str` (uuid4) | Gerado automaticamente |
| `descricao` | `str` | Não pode ser vazia nem só espaços |
| `valor` | `Decimal` | Deve ser > 0 (armazenado sempre positivo) |
| `tipo` | `TipoTransacao` | ENTRADA ou SAIDA (enum) |
| `data` | `date` | Default: hoje |
| `categoria_id` | `str` | Referência à categoria |

Método de domínio `valor_com_sinal()`: retorna `+valor` para ENTRADA e `-valor` para SAIDA. Usado pelo `CalcularSaldo` e `TotalPorCategoria`.

Validações no `__post_init__`: `DescricaoVaziaError`, `ValorInvalidoError`, `TipoInvalidoError`. Aceita `tipo` como string e converte para enum.

### Categoria

| Campo | Tipo | Regra |
|---|---|---|
| `id` | `str` (uuid4) | Gerado automaticamente |
| `nome` | `str` | Não pode ser vazio nem só espaços |
| `limite_mensal` | `Optional[Decimal]` | Se informado, deve ser >= 0 |

Validações no `__post_init__`: `NomeVazioError`, `LimiteInvalidoError`.

---

## Casos de uso

| Use Case | Classe | Método | Repositórios (ABCs) | HU |
|---|---|---|---|---|
| Criar Transação | `CriarTransacao` | `executar(descricao, valor, tipo, categoria_id, data?)` | `TransacaoRepository`, `CategoriaRepository` | HU-01 |
| Criar Categoria | `CriarCategoria` | `executar(nome, limite_mensal?)` | `CategoriaRepository` | HU-02 |
| Listar Transações | `ListarTransacoes` | `executar()` | `TransacaoRepository` | HU-01/03 |
| Calcular Saldo | `CalcularSaldo` | `executar()` | `TransacaoRepository` | HU-03 |
| Total por Categoria | `TotalPorCategoria` | `executar()` | `TransacaoRepository`, `CategoriaRepository` | HU-04 |

Todos seguem o mesmo padrão: classe com construtor que recebe ABCs por injeção, método `executar()` que orquestra.

**CriarTransacao** tem uma regra de aplicação (não de domínio): verifica se a `categoria_id` existe antes de criar a transação. Se não existir, lança `CategoriaInexistenteError`. A validação dos campos (valor > 0, etc.) fica na entidade.

**CalcularSaldo** usa `valor_com_sinal()` de cada transação e soma tudo com `sum()`. Retorna `Decimal("0")` se não houver transações.

**TotalPorCategoria** itera sobre cada categoria, busca suas transações com `listar_por_categoria()`, soma `valor_com_sinal()` e retorna uma lista de `TotalCategoria` (dataclass com `categoria_id`, `nome`, `total`).

---

## Histórias de Usuário

| HU | Como... | Quero... | Para... | Use Cases |
|---|---|---|---|---|
| HU-01 | usuário | registrar uma transação (entrada ou saída) | acompanhar minhas finanças | `CriarTransacao`, `ListarTransacoes` |
| HU-02 | usuário | criar categorias | organizar minhas transações | `CriarCategoria` |
| HU-03 | usuário | consultar meu saldo atual (entradas - saídas) | saber quanto tenho | `CalcularSaldo`, `ListarTransacoes` |
| HU-04 | usuário | ver o total por categoria | entender onde gasto mais | `TotalPorCategoria` |

---

## Endpoints da API REST

| Verbo | Rota | Use Case | Sucesso | Erro |
|---|---|---|---|---|
| `POST` | `/categorias` | `CriarCategoria` | 201 + JSON da categoria | 422 (regra violada) |
| `GET` | `/categorias` | repo direto | 200 + lista JSON | — |
| `POST` | `/transacoes` | `CriarTransacao` | 201 + JSON da transação | 404 (categoria inexistente), 422 (regra violada) |
| `GET` | `/transacoes` | `ListarTransacoes` | 200 + lista JSON | — |
| `GET` | `/saldo` | `CalcularSaldo` | 200 + `{"saldo": "..."}` | — |
| `GET` | `/relatorios/por-categoria` | `TotalPorCategoria` | 200 + `{"categorias": [...]}` | — |

Valores monetários trafegam como string nos JSONs para preservar `Decimal` sem perda de precisão (ex.: `"250.00"` e não `250.0`).

Tratamento de erros: exceções de domínio (`DominioError` e subclasses) são capturadas nas rotas e convertidas para HTTP. `CategoriaInexistenteError` retorna 404, demais erros de domínio retornam 422 com `{"erro": "mensagem"}`.

---

## Frontend web

O frontend é uma interface web servida pelo Flask via templates Jinja2. Fica na mesma camada que as rotas JSON (Camada 3 — Interface Adapters). Não contém regra de negócio; consome a API REST existente via `fetch()` em JavaScript.

| Rota | Página | O que faz |
|---|---|---|
| `/` | Dashboard | Mostra saldo, total de entradas/saídas, número de transações, totais por categoria com barras visuais, últimas 5 transações |
| `/ui/categorias` | Categorias | Formulário para criar categoria + tabela com categorias existentes |
| `/ui/transacoes` | Transações | Formulário para criar transação (com dropdown de categorias) + tabela com todas as transações |

Arquitetura do frontend:
- `app/routes/frontend_routes.py` — Blueprint que renderiza os templates. Nenhuma lógica de negócio.
- `app/templates/base.html` — Layout base com navbar e footer.
- `app/templates/index.html`, `categorias.html`, `transacoes.html` — páginas com JS inline que chama `fetch()` para a API.
- `app/static/js/app.js` — Funções utilitárias: `api()`, `formatCurrency()`, `formatDate()`, `esc()`, `toast()`.
- `app/static/css/style.css` — Tema escuro, responsivo, sem dependências externas.

O frontend respeita a Clean Architecture porque:
1. Não acessa diretamente os use cases ou o banco — só chama a API REST (que passa pelos use cases).
2. É apenas mais um adapter de entrega (assim como as rotas JSON).
3. Pode ser removido ou substituído por um SPA React, por exemplo, sem afetar nada nas camadas internas.

---

## Testes unitários

39 testes, todos passando. Divididos em dois grupos:

### Testes de domínio (`tests/domain/`)

Testam as regras de negócio das entidades diretamente, sem nenhum setup externo.

**`test_transacao.py` (11 testes):**
- Criação válida: entrada, saída, tipo como string, conversão para Decimal
- `valor_com_sinal()`: positivo para ENTRADA, negativo para SAIDA
- Regras violadas: valor zero, valor negativo, descrição vazia, descrição só espaços, tipo inválido

**`test_categoria.py` (7 testes):**
- Criação válida: sem limite, com limite, limite zero, conversão para Decimal
- Regras violadas: nome vazio, nome só espaços, limite negativo

### Testes de use case (`tests/use_cases/`)

Testam os use cases com **fakes in-memory**, isolados de Flask e SQLite. Isso prova o DIP na prática: o use case funciona com qualquer implementação da ABC.

Os fakes estão em `tests/use_cases/conftest.py`:
- `FakeTransacaoRepository` — guarda transações em `list`
- `FakeCategoriaRepository` — guarda categorias em `dict`

Ambos implementam as mesmas ABCs que os repositórios SQLite. São injetados via fixtures do pytest.

**`test_criar_categoria.py` (4 testes):**
- Caminho feliz: cria com sucesso, cria com limite
- Regra violada: nome vazio lança exceção
- Borda: verifica que a categoria é persistida no repositório

**`test_criar_transacao.py` (6 testes):**
- Caminho feliz: cria entrada, cria saída, com data específica
- Regra violada: categoria inexistente, valor negativo
- Borda: verifica que a transação é persistida

**`test_listar_transacoes.py` (3 testes):**
- Lista vazia, lista com transações, retorna cópia (não referência interna)

**`test_calcular_saldo.py` (4 testes):**
- Saldo zero sem transações
- Saldo = entradas - saídas
- Saldo negativo quando saídas maiores
- Saldo só com entradas

**`test_total_por_categoria.py` (4 testes):**
- Sem categorias: lista vazia
- Categoria sem transações: total zero
- Agrupamento correto por categoria
- Mistura entradas e saídas na mesma categoria

---

## Cobertura de testes

```
Name                                           Stmts   Miss  Cover
-------------------------------------------------------------------
domain/entities/categoria.py                      18      0   100%
domain/entities/transacao.py                      33      0   100%
domain/exceptions.py                               7      0   100%
use_cases/calcular_saldo.py                        8      0   100%
use_cases/criar_categoria.py                      11      0   100%
use_cases/criar_transacao.py                      21      0   100%
use_cases/interfaces/categoria_repository.py       9      0   100%
use_cases/interfaces/transacao_repository.py       9      0   100%
use_cases/listar_transacoes.py                     7      0   100%
use_cases/total_por_categoria.py                  21      0   100%
-------------------------------------------------------------------
TOTAL                                            144      0   100%
```

**100% de cobertura** em `domain/` e `use_cases/`. Requisito era >= 80%.

---

## Decisões técnicas

| Decisão | Justificativa |
|---|---|
| `Decimal` para valores monetários | Float perde precisão em operações financeiras. `Decimal("0.1") + Decimal("0.2") == Decimal("0.3")` funciona; com float, não. |
| IDs como uuid4 string | Evita acoplamento com autoincrement do banco. A entidade é responsável pela sua identidade, não a infraestrutura. |
| sqlite3 sem ORM | Mais didático para mostrar o padrão Adapter. O repositório faz a conversão manualmente entre entidades e rows. |
| Fakes manuais em vez de `unittest.mock` | Mais explícito: cada fake implementa a ABC concretamente, mostrando que o contrato é respeitado (LSP). Mocks esconderiam isso. |
| Valores como string no JSON | `Decimal` não é serializável nativamente em JSON. Enviar como string preserva a precisão. |
| Sem autenticação | O enunciado pede gerenciador pessoal, não multi-usuário. |
| Frontend via Jinja2 + fetch() | Sem dependência extra (React, Vue). O frontend consome a API REST que já existia, demonstrando que múltiplos adapters de entrega podem coexistir. |

---

## Critérios de Avaliação — mapeamento

| Critério (peso) | Como é atendido | Onde verificar |
|---|---|---|
| App funcional, >= 3 use cases, >= 2 entidades (4,0) | 5 use cases (`CriarTransacao`, `CriarCategoria`, `ListarTransacoes`, `CalcularSaldo`, `TotalPorCategoria`), 2 entidades (`Transacao`, `Categoria`), 6 endpoints REST funcionais + frontend web | `use_cases/`, `domain/entities/`, `app/routes/` |
| Clean Architecture correta (2,0) | 4 camadas em pastas separadas (`domain/`, `use_cases/`, `app/`, `infra/`); dependências apontam só para dentro; golden rule respeitada; diagrama acima | Verificar imports de cada módulo |
| SOLID correto (2,0) | SRP/OCP/LSP/ISP/DIP aplicados e comentados no código; tabela detalhada acima com arquivo, aplicação e justificativa para cada princípio | Comentários nos arquivos + tabela neste README |
| Testes unitários dos use cases (1,0) | 39 testes, use cases testados com fakes in-memory, isolados de Flask/SQLite, 100% de cobertura em `domain/` e `use_cases/` | `pytest --cov` |
| PEP-8 (1,0) | ruff configurado no `pyproject.toml` (E, F, W, I, N), zero warnings | `ruff check .` |
