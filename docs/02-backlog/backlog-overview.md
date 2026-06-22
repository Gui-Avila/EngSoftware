# Backlog Overview — FinTrack

## Árvore do Backlog

```
EPIC-01  Gestão de Categorias
└── F-01  Cadastro e listagem de categorias
    └── US-02  Criar categoria de transação

EPIC-02  Gestão de Transações
└── F-02  Registro e listagem de transações
    └── US-01  Registrar transação financeira

EPIC-03  Relatórios Financeiros
├── F-03  Consulta de saldo
│   └── US-03  Consultar saldo atual
└── F-04  Relatório por categoria
    └── US-04  Visualizar totais por categoria

(Enablers — itens técnicos que viabilizam as features)
├── EN-01  Estrutura Clean Architecture + Injeção de Dependências
├── EN-02  Camada de persistência SQLite
└── EN-03  Interface web (Dashboard, Categorias, Transações)
```

## Tabela Mestre

| ID | Tipo | Título | Épico | SP | Status | Código principal |
|---|---|---|---|---|---|---|
| US-01 | Story | Registrar transação financeira | EPIC-02 | 5 | Done | `use_cases/criar_transacao.py` |
| US-02 | Story | Criar categoria de transação | EPIC-01 | 3 | Done | `use_cases/criar_categoria.py` |
| US-03 | Story | Consultar saldo atual | EPIC-03 | 3 | Done | `use_cases/calcular_saldo.py`, `use_cases/listar_transacoes.py` |
| US-04 | Story | Visualizar totais por categoria | EPIC-03 | 5 | Done | `use_cases/total_por_categoria.py` |
| EN-01 | Enabler | Estrutura Clean Architecture + DI | — | 3 | Done | `app/main.py`, `use_cases/interfaces/` |
| EN-02 | Enabler | Camada de persistência SQLite | — | 5 | Done | `infra/` |
| EN-03 | Enabler | Interface web | — | 5 | Done | `app/templates/`, `app/static/`, `app/routes/frontend_routes.py` |

**Total:** 29 Story Points

O backlog segue o princípio de backlog emergente: os itens da sprint atual
(esta única sprint) estão detalhados com critérios de aceitação e
rastreabilidade. Itens fora do escopo (edição/exclusão, autenticação, alertas
de limite) foram registrados como ice box no backlog mas não refinados.
