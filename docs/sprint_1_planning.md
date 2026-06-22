# Sprint 1 — Planning

> Registro da cerimônia de Sprint Planning realizada no início da Sprint 1.

---

## Dados da Sprint

| Campo | Valor |
|---|---|
| **Sprint** | Sprint 1 |
| **Duração** | 2 semanas |
| **Início** | 09/06/2025 |
| **Fim** | 22/06/2025 |
| **Capacidade da equipe** | 3 desenvolvedores × 10 dias × ~4h/dia = ~120h |
| **Velocidade estimada** | 43 SP (primeira sprint — sem histórico) |

---

## Sprint Goal

> **Entregar um gerenciador financeiro pessoal funcional** com cadastro de
> categorias, registro de transações, consulta de saldo e relatório por
> categoria, seguindo Clean Architecture, SOLID e com cobertura de testes
> unitários ≥ 80%.

---

## Itens selecionados para a Sprint

### User Stories

| ID | User Story | SP | Responsável |
|---|---|---|---|
| HU-01 | Registrar transação financeira | 5 | Dev 1 |
| HU-02 | Criar categoria de transação | 3 | Dev 2 |
| HU-03 | Consultar saldo atual | 3 | Dev 1 |
| HU-04 | Visualizar totais por categoria | 5 | Dev 3 |

### Technical Tasks

| ID | Task | SP | Responsável |
|---|---|---|---|
| TK-01 | Setup do projeto (estrutura Clean Architecture) | 3 | Dev 1 |
| TK-02 | Modelar entidades de domínio (Transacao + Categoria) | 3 | Dev 2 |
| TK-03 | Implementar repositórios SQLite | 5 | Dev 3 |
| TK-04 | Testes unitários (domínio + use cases) | 5 | Todos |
| TK-05 | Frontend web (Dashboard, Categorias, Transações) | 8 | Dev 1 |
| TK-06 | Configurar Ruff + PEP-8 | 1 | Dev 2 |
| TK-07 | Documentação (README) | 2 | Dev 3 |

**Total comprometido:** 43 Story Points

---

## Decomposição e Dependências

```
TK-01 (Setup projeto)
  │
  ├──▶ TK-02 (Entidades de domínio)
  │       │
  │       ├──▶ HU-02 (Criar categoria)
  │       │       │
  │       │       └──▶ HU-01 (Registrar transação) ← depende de categoria existir
  │       │               │
  │       │               ├──▶ HU-03 (Consultar saldo)
  │       │               │
  │       │               └──▶ HU-04 (Totais por categoria)
  │       │
  │       └──▶ TK-03 (Repositórios SQLite)
  │
  ├──▶ TK-06 (Ruff / PEP-8) ← paralelo
  │
  └──▶ TK-04 (Testes) ← incremental, acompanha cada HU

TK-05 (Frontend) ← após endpoints prontos
TK-07 (README) ← final da sprint
```

---

## Acordos da Sprint

1. **Branching:** desenvolvimento na branch `main` com commits atômicos
   e mensagens descritivas.
2. **Code review:** revisão informal entre pares antes de merge.
3. **Testes:** cada use case deve ter testes antes de ser considerado Done.
4. **Daily standup:** check-in diário assíncrono (mensagem no grupo).
5. **Definition of Done:** conforme documentado em
   [`definition_of_done.md`](definition_of_done.md).

---

## Riscos Identificados

| Risco | Probabilidade | Impacto | Mitigação |
|---|---|---|---|
| Dificuldade com Clean Architecture | Média | Alto | Estudar material de referência antes de codar |
| Tempo insuficiente para frontend | Média | Médio | Frontend é "Should Have"; priorizar backend + testes |
| Bugs de integração SQLite ↔ entidades | Baixa | Médio | Testes isolados com fakes garantem lógica correta |
| Conflitos de merge no Git | Baixa | Baixo | Comunicação no daily + commits frequentes |
