# Sprint 1 — Board (Simulação Jira)

> Simulação do quadro Kanban/Scrum Board do Jira ao longo da Sprint 1.
> Cada seção representa o estado do board em um momento da sprint.

---

## Legenda

| Coluna | Significado |
|---|---|
| 📋 **TO DO** | Item planejado, ainda não iniciado |
| 🔨 **IN PROGRESS** | Item em desenvolvimento ativo |
| 👀 **IN REVIEW** | Aguardando revisão de código |
| ✅ **DONE** | Item concluído e atende ao DoD |

Etiquetas: `🔴 bug` · `🟢 story` · `🔵 task` · `🟡 improvement`

---

## 📅 Dia 1 (09/06) — Início da Sprint

### 📋 TO DO
| Key | Tipo | Resumo | SP | Assignee |
|---|---|---|---|---|
| FT-HU-01 | 🟢 Story | Registrar transação financeira | 5 | Dev 1 |
| FT-HU-02 | 🟢 Story | Criar categoria de transação | 3 | Dev 2 |
| FT-HU-03 | 🟢 Story | Consultar saldo atual | 3 | Dev 1 |
| FT-HU-04 | 🟢 Story | Visualizar totais por categoria | 5 | Dev 3 |
| FT-TK-02 | 🔵 Task | Modelar entidades de domínio | 3 | Dev 2 |
| FT-TK-03 | 🔵 Task | Implementar repositórios SQLite | 5 | Dev 3 |
| FT-TK-04 | 🔵 Task | Testes unitários | 5 | Todos |
| FT-TK-05 | 🔵 Task | Frontend web | 8 | Dev 1 |
| FT-TK-06 | 🔵 Task | Configurar Ruff + PEP-8 | 1 | Dev 2 |
| FT-TK-07 | 🔵 Task | Documentação (README) | 2 | Dev 3 |

### 🔨 IN PROGRESS
| Key | Tipo | Resumo | SP | Assignee |
|---|---|---|---|---|
| FT-TK-01 | 🔵 Task | Setup do projeto (Clean Architecture) | 3 | Dev 1 |

### ✅ DONE
_(vazio)_

---

## 📅 Dia 2–3 (10–11/06) — Fundação

### 📋 TO DO
| Key | Tipo | Resumo | SP | Assignee |
|---|---|---|---|---|
| FT-HU-01 | 🟢 Story | Registrar transação financeira | 5 | Dev 1 |
| FT-HU-03 | 🟢 Story | Consultar saldo atual | 3 | Dev 1 |
| FT-HU-04 | 🟢 Story | Visualizar totais por categoria | 5 | Dev 3 |
| FT-TK-03 | 🔵 Task | Implementar repositórios SQLite | 5 | Dev 3 |
| FT-TK-04 | 🔵 Task | Testes unitários | 5 | Todos |
| FT-TK-05 | 🔵 Task | Frontend web | 8 | Dev 1 |
| FT-TK-07 | 🔵 Task | Documentação (README) | 2 | Dev 3 |

### 🔨 IN PROGRESS
| Key | Tipo | Resumo | SP | Assignee |
|---|---|---|---|---|
| FT-TK-02 | 🔵 Task | Modelar entidades de domínio | 3 | Dev 2 |
| FT-HU-02 | 🟢 Story | Criar categoria de transação | 3 | Dev 2 |
| FT-TK-06 | 🔵 Task | Configurar Ruff + PEP-8 | 1 | Dev 2 |

### ✅ DONE
| Key | Tipo | Resumo | SP | Completado |
|---|---|---|---|---|
| FT-TK-01 | 🔵 Task | Setup do projeto | 3 | 10/06 |

---

## 📅 Dia 4–5 (12–13/06) — Entidades e Categorias

### 📋 TO DO
| Key | Tipo | Resumo | SP | Assignee |
|---|---|---|---|---|
| FT-HU-03 | 🟢 Story | Consultar saldo atual | 3 | Dev 1 |
| FT-HU-04 | 🟢 Story | Visualizar totais por categoria | 5 | Dev 3 |
| FT-TK-05 | 🔵 Task | Frontend web | 8 | Dev 1 |
| FT-TK-07 | 🔵 Task | Documentação (README) | 2 | Dev 3 |

### 🔨 IN PROGRESS
| Key | Tipo | Resumo | SP | Assignee |
|---|---|---|---|---|
| FT-HU-01 | 🟢 Story | Registrar transação financeira | 5 | Dev 1 |
| FT-TK-03 | 🔵 Task | Implementar repositórios SQLite | 5 | Dev 3 |
| FT-TK-04 | 🔵 Task | Testes unitários (entidades) | 5 | Todos |

### 👀 IN REVIEW
| Key | Tipo | Resumo | SP | Reviewer |
|---|---|---|---|---|
| FT-HU-02 | 🟢 Story | Criar categoria de transação | 3 | Dev 1 |

### ✅ DONE
| Key | Tipo | Resumo | SP | Completado |
|---|---|---|---|---|
| FT-TK-01 | 🔵 Task | Setup do projeto | 3 | 10/06 |
| FT-TK-02 | 🔵 Task | Modelar entidades de domínio | 3 | 12/06 |
| FT-TK-06 | 🔵 Task | Configurar Ruff + PEP-8 | 1 | 11/06 |

---

## 📅 Dia 6–7 (14–15/06) — Transações e Saldo (fim de semana)

### 📋 TO DO
| Key | Tipo | Resumo | SP | Assignee |
|---|---|---|---|---|
| FT-TK-05 | 🔵 Task | Frontend web | 8 | Dev 1 |
| FT-TK-07 | 🔵 Task | Documentação (README) | 2 | Dev 3 |

### 🔨 IN PROGRESS
| Key | Tipo | Resumo | SP | Assignee |
|---|---|---|---|---|
| FT-HU-03 | 🟢 Story | Consultar saldo atual | 3 | Dev 1 |
| FT-HU-04 | 🟢 Story | Visualizar totais por categoria | 5 | Dev 3 |
| FT-TK-04 | 🔵 Task | Testes unitários (use cases) | 5 | Todos |

### ✅ DONE
| Key | Tipo | Resumo | SP | Completado |
|---|---|---|---|---|
| FT-TK-01 | 🔵 Task | Setup do projeto | 3 | 10/06 |
| FT-TK-02 | 🔵 Task | Modelar entidades de domínio | 3 | 12/06 |
| FT-TK-06 | 🔵 Task | Configurar Ruff + PEP-8 | 1 | 11/06 |
| FT-HU-02 | 🟢 Story | Criar categoria de transação | 3 | 13/06 |
| FT-HU-01 | 🟢 Story | Registrar transação financeira | 5 | 14/06 |
| FT-TK-03 | 🔵 Task | Implementar repositórios SQLite | 5 | 14/06 |

---

## 📅 Dia 8–9 (16–17/06) — Relatórios e Testes

### 📋 TO DO
| Key | Tipo | Resumo | SP | Assignee |
|---|---|---|---|---|
| FT-TK-07 | 🔵 Task | Documentação (README) | 2 | Dev 3 |

### 🔨 IN PROGRESS
| Key | Tipo | Resumo | SP | Assignee |
|---|---|---|---|---|
| FT-TK-05 | 🔵 Task | Frontend web | 8 | Dev 1 |

### 👀 IN REVIEW
| Key | Tipo | Resumo | SP | Reviewer |
|---|---|---|---|---|
| FT-TK-04 | 🔵 Task | Testes unitários (39 testes) | 5 | Dev 1 |

### ✅ DONE
| Key | Tipo | Resumo | SP | Completado |
|---|---|---|---|---|
| FT-TK-01 | 🔵 Task | Setup do projeto | 3 | 10/06 |
| FT-TK-02 | 🔵 Task | Modelar entidades de domínio | 3 | 12/06 |
| FT-TK-06 | 🔵 Task | Configurar Ruff + PEP-8 | 1 | 11/06 |
| FT-HU-02 | 🟢 Story | Criar categoria de transação | 3 | 13/06 |
| FT-HU-01 | 🟢 Story | Registrar transação financeira | 5 | 14/06 |
| FT-TK-03 | 🔵 Task | Implementar repositórios SQLite | 5 | 14/06 |
| FT-HU-03 | 🟢 Story | Consultar saldo atual | 3 | 16/06 |
| FT-HU-04 | 🟢 Story | Visualizar totais por categoria | 5 | 17/06 |

---

## 📅 Dia 10–12 (18–20/06) — Frontend e Polimento

### 🔨 IN PROGRESS
| Key | Tipo | Resumo | SP | Assignee |
|---|---|---|---|---|
| FT-TK-07 | 🔵 Task | Documentação (README) | 2 | Dev 3 |

### 👀 IN REVIEW
| Key | Tipo | Resumo | SP | Reviewer |
|---|---|---|---|---|
| FT-TK-05 | 🔵 Task | Frontend web (3 páginas) | 8 | Dev 2 |

### ✅ DONE
| Key | Tipo | Resumo | SP | Completado |
|---|---|---|---|---|
| FT-TK-01 | 🔵 Task | Setup do projeto | 3 | 10/06 |
| FT-TK-02 | 🔵 Task | Modelar entidades de domínio | 3 | 12/06 |
| FT-TK-06 | 🔵 Task | Configurar Ruff + PEP-8 | 1 | 11/06 |
| FT-HU-02 | 🟢 Story | Criar categoria de transação | 3 | 13/06 |
| FT-HU-01 | 🟢 Story | Registrar transação financeira | 5 | 14/06 |
| FT-TK-03 | 🔵 Task | Implementar repositórios SQLite | 5 | 14/06 |
| FT-HU-03 | 🟢 Story | Consultar saldo atual | 3 | 16/06 |
| FT-HU-04 | 🟢 Story | Visualizar totais por categoria | 5 | 17/06 |
| FT-TK-04 | 🔵 Task | Testes unitários (39 testes, 100% cov) | 5 | 17/06 |

---

## 📅 Dia 13–14 (21–22/06) — Finalização 🏁

### ✅ DONE — Sprint Completa!
| Key | Tipo | Resumo | SP | Completado |
|---|---|---|---|---|
| FT-TK-01 | 🔵 Task | Setup do projeto (Clean Architecture) | 3 | 10/06 |
| FT-TK-06 | 🔵 Task | Configurar Ruff + PEP-8 | 1 | 11/06 |
| FT-TK-02 | 🔵 Task | Modelar entidades de domínio | 3 | 12/06 |
| FT-HU-02 | 🟢 Story | Criar categoria de transação | 3 | 13/06 |
| FT-HU-01 | 🟢 Story | Registrar transação financeira | 5 | 14/06 |
| FT-TK-03 | 🔵 Task | Implementar repositórios SQLite | 5 | 14/06 |
| FT-HU-03 | 🟢 Story | Consultar saldo atual | 3 | 16/06 |
| FT-HU-04 | 🟢 Story | Visualizar totais por categoria | 5 | 17/06 |
| FT-TK-04 | 🔵 Task | Testes unitários | 5 | 17/06 |
| FT-TK-05 | 🔵 Task | Frontend web | 8 | 20/06 |
| FT-TK-07 | 🔵 Task | Documentação (README) | 2 | 22/06 |

**Total entregue:** 43 / 43 SP (100%)

---

## Burndown (resumo textual)

```
SP Restantes
43 |████████████████████████████████████████████
40 |██████████████████████████████████████████    ← TK-01 done
37 |████████████████████████████████████████      ← TK-02 done
36 |███████████████████████████████████████       ← TK-06 done
33 |████████████████████████████████████          ← HU-02 done
28 |███████████████████████████████               ← HU-01 done
23 |██████████████████████████                    ← TK-03 done
20 |███████████████████████                       ← HU-03 done
15 |██████████████████                            ← HU-04 done
10 |████████████                                  ← TK-04 done
 2 |██                                            ← TK-05 done
 0 |                                              ← TK-07 done 🏁
   +-----+-----+-----+-----+-----+-----+-----
   D1    D3    D5    D7    D9    D11   D13
```

Sprint ideal: linha reta de 43→0 em 14 dias.
Sprint real: leve acúmulo nos dias iniciais (setup), aceleração na segunda semana.
