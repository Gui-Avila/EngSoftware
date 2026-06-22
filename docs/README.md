# Documentação de Engenharia — FinTrack

Esta pasta contém os artefatos de gestão ágil e engenharia de requisitos que
conduziram o desenvolvimento do FinTrack. Cada documento ancora-se no código
que existe no repositório — nenhum item de backlog aponta para algo que não
foi implementado.

## Artefatos

| Artefato | Arquivo | O que documenta |
|---|---|---|
| Visão do Produto | [01-product/product-vision.md](01-product/product-vision.md) | Público-alvo, proposta de valor, escopo |
| Personas | [01-product/personas.md](01-product/personas.md) | Perfis de usuário que orientam as histórias |
| Stakeholders | [01-product/stakeholders.md](01-product/stakeholders.md) | Partes interessadas e seu nível de influência |
| Backlog Overview | [02-backlog/backlog-overview.md](02-backlog/backlog-overview.md) | Árvore Épico → Feature → História e tabela mestre |
| Épicos | [02-backlog/epics.md](02-backlog/epics.md) | Descrição e features de cada épico |
| Features | [02-backlog/features.md](02-backlog/features.md) | Quebra ARO → PBIs → Histórias |
| US-01 | [02-backlog/user-stories/US-01-registrar-transacao.md](02-backlog/user-stories/US-01-registrar-transacao.md) | Registrar transação financeira |
| US-02 | [02-backlog/user-stories/US-02-criar-categoria.md](02-backlog/user-stories/US-02-criar-categoria.md) | Criar categoria de transação |
| US-03 | [02-backlog/user-stories/US-03-consultar-saldo.md](02-backlog/user-stories/US-03-consultar-saldo.md) | Consultar saldo atual |
| US-04 | [02-backlog/user-stories/US-04-total-por-categoria.md](02-backlog/user-stories/US-04-total-por-categoria.md) | Visualizar totais por categoria |
| Definition of Ready | [03-process/definition-of-ready.md](03-process/definition-of-ready.md) | Checklist INVEST para entrada na sprint |
| Definition of Done | [03-process/definition-of-done.md](03-process/definition-of-done.md) | Critérios de conclusão com NFRs |
| Matriz de Story Points | [03-process/story-point-matrix.md](03-process/story-point-matrix.md) | Escala Fibonacci e justificativa por história |
| Sprint Plan | [03-process/sprint-plan.md](03-process/sprint-plan.md) | Equipe, capacidade, goal e itens comprometidos |
| Board | [04-board/board.md](04-board/board.md) | Quadro Kanban com estado final da sprint |
| Matriz de Rastreabilidade | [05-traceability/traceability-matrix.md](05-traceability/traceability-matrix.md) | História ↔ Use Case ↔ Código ↔ Teste |

## Como ler

1. **Visão e contexto** — comece por `01-product/` para entender o produto e quem o usa.
2. **Backlog** — siga para `02-backlog/` para ver a hierarquia Épico → Feature → História.
3. **Histórias individuais** — cada arquivo em `02-backlog/user-stories/` tem a narrativa, critérios BDD, regras de negócio e rastreabilidade para o código.
4. **Processo** — `03-process/` documenta DoR, DoD, estimativas e planejamento da sprint.
5. **Board e rastreabilidade** — `04-board/` e `05-traceability/` fecham o ciclo: o que foi feito e como cada item de processo aponta para código real.
