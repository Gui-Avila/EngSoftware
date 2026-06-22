# Product Backlog — FinTrack

> Backlog priorizado por valor de negócio (MoSCoW) e estimado em Story Points
> (Fibonacci). Todos os itens referem-se à Sprint 1.

---

## Épicos

| ID | Épico | Descrição |
|---|---|---|
| EP-01 | Gestão de Categorias | Permitir ao usuário criar e visualizar categorias de despesa/receita |
| EP-02 | Gestão de Transações | Permitir ao usuário registrar, listar e acompanhar movimentações |
| EP-03 | Relatórios Financeiros | Oferecer visões consolidadas (saldo, totais por categoria) |
| EP-04 | Infraestrutura & Qualidade | Arquitetura, persistência, testes, linting |

---

## Features

| ID | Feature | Épico | Prioridade |
|---|---|---|---|
| FT-01 | Cadastro de Categorias | EP-01 | Must Have |
| FT-02 | Listagem de Categorias | EP-01 | Must Have |
| FT-03 | Registro de Transações | EP-02 | Must Have |
| FT-04 | Listagem de Transações | EP-02 | Must Have |
| FT-05 | Consulta de Saldo | EP-03 | Must Have |
| FT-06 | Relatório por Categoria | EP-03 | Should Have |
| FT-07 | Interface Web (Frontend) | EP-02 | Should Have |
| FT-08 | Arquitetura Clean + SOLID | EP-04 | Must Have |
| FT-09 | Testes Unitários | EP-04 | Must Have |
| FT-10 | Linting (PEP-8 / Ruff) | EP-04 | Must Have |

---

## Backlog de User Stories (priorizado)

| Rank | ID | User Story (resumo) | Feature | SP | MoSCoW | Status |
|---|---|---|---|---|---|---|
| 1 | HU-01 | Registrar transação financeira | FT-03 | 5 | Must | ✅ Done |
| 2 | HU-02 | Criar categoria de transação | FT-01 | 3 | Must | ✅ Done |
| 3 | HU-03 | Consultar saldo atual | FT-05 | 3 | Must | ✅ Done |
| 4 | HU-04 | Visualizar totais por categoria | FT-06 | 5 | Should | ✅ Done |
| 5 | TK-01 | Setup do projeto (Clean Architecture) | FT-08 | 3 | Must | ✅ Done |
| 6 | TK-02 | Modelar entidades de domínio | FT-08 | 3 | Must | ✅ Done |
| 7 | TK-03 | Implementar repositórios SQLite | FT-08 | 5 | Must | ✅ Done |
| 8 | TK-04 | Testes unitários (domínio + use cases) | FT-09 | 5 | Must | ✅ Done |
| 9 | TK-05 | Frontend web (Dashboard, Categorias, Transações) | FT-07 | 8 | Should | ✅ Done |
| 10 | TK-06 | Configurar Ruff + PEP-8 | FT-10 | 1 | Must | ✅ Done |
| 11 | TK-07 | Documentação (README) | FT-10 | 2 | Must | ✅ Done |

**Total Sprint 1:** 43 Story Points

---

## Itens não priorizados (Ice Box)

| ID | Item | Motivo |
|---|---|---|
| ICE-01 | Editar / excluir transação | Fora do escopo da A2 |
| ICE-02 | Editar / excluir categoria | Fora do escopo da A2 |
| ICE-03 | Autenticação multi-usuário | Complexidade além do necessário |
| ICE-04 | Alerta de limite mensal por categoria | Nice-to-have para sprint futura |
| ICE-05 | Containerização (Docker) | Não obrigatório na A2 |
| ICE-06 | CI/CD (GitHub Actions) | Não obrigatório na A2 |
