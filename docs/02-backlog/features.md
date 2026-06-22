# Features — FinTrack

## F-01 — Cadastro e Listagem de Categorias

**Épico pai:** EPIC-01

**Descrição:** o usuário pode criar categorias com nome e limite mensal
opcional, e visualizar a lista de categorias cadastradas.

### Quebra em PBIs (modelo ARO — Ação + Resultado + Objeto)

| PBI (ARO) | História derivada |
|---|---|
| Cadastrar → categoria criada e persistida → Categoria | US-02 |
| Listar → categorias exibidas → Categorias | US-02 (endpoint GET incluso) |

**Histórias geradas:** US-02

---

## F-02 — Registro e Listagem de Transações

**Épico pai:** EPIC-02

**Descrição:** o usuário pode registrar transações (entrada ou saída)
associadas a uma categoria existente, informando descrição, valor, tipo
e data opcional. Também pode listar todas as transações.

### Quebra em PBIs (modelo ARO)

| PBI (ARO) | História derivada |
|---|---|
| Registrar → transação validada e persistida → Transação | US-01 |
| Listar → transações exibidas → Transações | US-01 (endpoint GET incluso) |

**Histórias geradas:** US-01

---

## F-03 — Consulta de Saldo

**Épico pai:** EPIC-03

**Descrição:** o usuário pode consultar o saldo financeiro atual,
calculado como a soma das entradas menos a soma das saídas.

### Quebra em PBIs (modelo ARO)

| PBI (ARO) | História derivada |
|---|---|
| Consultar → saldo calculado e retornado → Saldo | US-03 |
| Listar → transações disponíveis para conferência → Transações | US-03 (usa `ListarTransacoes`) |

**Histórias geradas:** US-03

---

## F-04 — Relatório por Categoria

**Épico pai:** EPIC-03

**Descrição:** o usuário pode visualizar o total líquido de movimentações
agrupado por categoria, identificando onde gasta e onde recebe mais.

### Quebra em PBIs (modelo ARO)

| PBI (ARO) | História derivada |
|---|---|
| Consultar → totais agrupados por categoria → Relatório | US-04 |

**Histórias geradas:** US-04
