# Sprint Plan — Sprint 1

## Equipe e papéis

| Papel | Membro |
|---|---|
| Product Owner / Desenvolvedor | Guilherme |
| Scrum Master / Desenvolvedor | Membro 2 |
| Desenvolvedor | Membro 3 |

## Capacidade

| Parâmetro | Valor |
|---|---|
| Duração da sprint | 2 semanas (10 dias úteis) |
| Desenvolvedores | 3 |
| Horas úteis/dia por dev | ~4h (projeto acadêmico, conciliando com aulas) |
| Capacidade bruta | 3 × 10 × 4 = 120h |
| Fator de foco | ~0.75 (reuniões, estudo de material, setup) |
| Capacidade líquida | ~90h |

## Sprint Goal

Entregar um gerenciador financeiro pessoal funcional com cadastro de
categorias, registro de transações, consulta de saldo e relatório por
categoria, seguindo Clean Architecture e SOLID, com cobertura de testes
unitários ≥ 80% em domínio e use cases.

## Itens comprometidos

### User Stories

| ID | Título | SP |
|---|---|---|
| US-02 | Criar categoria de transação | 3 |
| US-01 | Registrar transação financeira | 5 |
| US-03 | Consultar saldo atual | 3 |
| US-04 | Visualizar totais por categoria | 5 |
| | **Subtotal Stories** | **16** |

### Enablers

| ID | Título | SP |
|---|---|---|
| EN-01 | Estrutura Clean Architecture + Injeção de Dependências | 3 |
| EN-02 | Camada de persistência SQLite | 5 |
| EN-03 | Interface web (Dashboard, Categorias, Transações) | 5 |
| | **Subtotal Enablers** | **13** |

### Total comprometido: 29 SP

## Ordem de execução (dependências)

```
EN-01 (setup)
 ├─▸ US-02 (categorias — sem dependências de negócio)
 │    └─▸ US-01 (transações — depende de categoria existir)
 │         ├─▸ US-03 (saldo — depende de transações existirem)
 │         └─▸ US-04 (totais — depende de transações e categorias)
 ├─▸ EN-02 (SQLite — paralelo às stories, mesma interface)
 └─▸ EN-03 (frontend — após endpoints prontos)
```

## Velocidade

Sprint 1 — sem histórico. Os 29 SP representam a estimativa inicial.
A velocidade real será conhecida ao final da sprint e servirá de base
para sprints futuras.
