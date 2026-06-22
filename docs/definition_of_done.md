# Definition of Done (DoD) — FinTrack

> Critérios acordados pela equipe para que um item do backlog seja considerado
> **"Done"** e potencialmente entregável.

---

## Critérios Gerais

| # | Critério | Verificação |
|---|---|---|
| 1 | O código compila/executa sem erros | `python run.py` inicia sem exceções |
| 2 | Todos os critérios de aceitação da user story foram atendidos | Checklist da HU marcado |
| 3 | Testes unitários escritos e passando | `pytest` retorna 0 falhas |
| 4 | Cobertura de testes ≥ 80% nas camadas de domínio e use cases | `pytest --cov` |
| 5 | Código segue PEP-8 / convenções do Ruff | `ruff check .` sem erros |
| 6 | Código commitado no repositório Git com mensagem descritiva | `git log` |
| 7 | Nenhuma dependência de infraestrutura nos use cases | Imports verificados |
| 8 | Princípios SOLID aplicados e documentados | Revisão por pares |

---

## Critérios por Camada (Clean Architecture)

### Domain (Entidades)

- [ ] Entidade é um objeto puro Python (sem dependências externas)
- [ ] Validações de negócio estão na entidade (fail fast)
- [ ] Exceções de domínio são específicas e descritivas
- [ ] Testes unitários cobrem cenários válidos e inválidos

### Use Cases

- [ ] Use case depende apenas de interfaces (ABCs), nunca de implementações
- [ ] Método principal é `executar()` com parâmetros explícitos
- [ ] Lógica de negócio está isolada de HTTP, SQL e frameworks
- [ ] Testes usam fakes/mocks que implementam as mesmas interfaces
- [ ] Todos os fluxos (happy path + exceções) estão testados

### Interface Adapters (Rotas Flask)

- [ ] Rotas fazem apenas parsing de request e formatação de response
- [ ] Lógica de negócio é delegada ao use case correspondente
- [ ] Códigos HTTP corretos (201 para criação, 200 para consulta, 4xx para erros)
- [ ] Valores monetários serializados como string (precisão Decimal)

### Frameworks & Drivers (Infra)

- [ ] Repositório SQLite implementa a mesma ABC que o fake de teste (LSP)
- [ ] Mapeamento entidade ↔ row é feito no repositório, não na entidade
- [ ] DDL do banco é idempotente (`CREATE TABLE IF NOT EXISTS`)

---

## Critérios de Qualidade de Código

| Princípio SOLID | Verificação |
|---|---|
| **SRP** | Cada classe tem uma única responsabilidade |
| **OCP** | Novos use cases/repositórios não exigem alterar código existente |
| **LSP** | Fakes e SQLite repos são intercambiáveis via interface |
| **ISP** | Interfaces de repositório são enxutas e específicas |
| **DIP** | Use cases dependem de abstrações (ABCs), não de SQLite |
