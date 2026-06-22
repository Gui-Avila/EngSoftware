# Sprint 1 — Review & Retrospectiva

> Registro das cerimônias de Sprint Review e Sprint Retrospective
> realizadas ao final da Sprint 1.

---

## Sprint Review

### Dados da Sprint

| Métrica | Valor |
|---|---|
| **Sprint Goal** | Entregar gerenciador financeiro pessoal com Clean Architecture |
| **Goal atingido?** | ✅ Sim |
| **SP comprometidos** | 43 |
| **SP entregues** | 43 (100%) |
| **User Stories entregues** | 4 / 4 |
| **Technical Tasks entregues** | 7 / 7 |
| **Testes totais** | 39 (passando) |
| **Cobertura (domínio + use cases)** | 100% |
| **Bugs encontrados em review** | 0 |

### Demo — Funcionalidades Entregues

#### 1. Cadastro de Categorias (HU-02)
- Formulário web para criar categorias com nome e limite mensal opcional
- API REST `POST /categorias` e `GET /categorias`
- Validações: nome obrigatório, limite ≥ 0
- **Resultado:** funcionando conforme critérios de aceitação

#### 2. Registro de Transações (HU-01)
- Formulário web com seleção de categoria via dropdown
- Suporte a ENTRADA e SAIDA com data opcional
- API REST `POST /transacoes` e `GET /transacoes`
- Validações: valor > 0, descrição obrigatória, categoria existente
- **Resultado:** funcionando conforme critérios de aceitação

#### 3. Consulta de Saldo (HU-03)
- Dashboard exibe saldo atual (entradas − saídas)
- Cards separados para total de entradas, total de saídas e contagem
- API REST `GET /saldo`
- **Resultado:** funcionando conforme critérios de aceitação

#### 4. Relatório por Categoria (HU-04)
- Dashboard exibe tabela com totais por categoria e barras visuais
- API REST `GET /relatorios/por-categoria`
- **Resultado:** funcionando conforme critérios de aceitação

### Feedback do Stakeholder (Professor)

> _Aguardando apresentação._

---

## Métricas de Qualidade

### Testes

| Camada | Arquivo de Teste | Nº de Testes |
|---|---|---|
| Domínio | `test_transacao.py` | 11 |
| Domínio | `test_categoria.py` | 7 |
| Use Case | `test_criar_transacao.py` | 6 |
| Use Case | `test_criar_categoria.py` | 4 |
| Use Case | `test_listar_transacoes.py` | 3 |
| Use Case | `test_calcular_saldo.py` | 4 |
| Use Case | `test_total_por_categoria.py` | 4 |
| **Total** | | **39** |

### Cobertura

| Camada | Statements | Missed | Cobertura |
|---|---|---|---|
| `domain/` | 72 | 0 | 100% |
| `use_cases/` | 72 | 0 | 100% |
| **Total** | **144** | **0** | **100%** |

### Clean Architecture — Compliance

| Regra | Status |
|---|---|
| Entidades não importam de camadas externas | ✅ |
| Use cases dependem apenas de ABCs | ✅ |
| Rotas Flask não contêm lógica de negócio | ✅ |
| Repositórios SQLite implementam as ABCs | ✅ |
| Fakes de teste implementam as mesmas ABCs | ✅ |

### SOLID — Compliance

| Princípio | Aplicação | Status |
|---|---|---|
| **SRP** | Cada use case = uma responsabilidade | ✅ |
| **OCP** | Novos repos não alteram use cases | ✅ |
| **LSP** | Fakes e SQLite intercambiáveis | ✅ |
| **ISP** | Interfaces de repo enxutas | ✅ |
| **DIP** | Use cases → ABCs, não SQLite | ✅ |

---

## Sprint Retrospective

### O que funcionou bem 👍

1. **Estrutura Clean Architecture desde o dia 1** — definir a arquitetura
   antes de codar economizou retrabalho significativo.
2. **Testes com fakes** — testar use cases sem banco de dados real tornou o
   ciclo de desenvolvimento muito rápido (`pytest` roda em <1s).
3. **Entidades com validação** — erros são capturados no domínio antes de
   chegar ao banco, garantindo integridade.
4. **Separação frontend/backend** — o frontend consome a API REST, o que
   permitiu desenvolver as camadas em paralelo.

### O que pode melhorar 🔧

1. **Faltaram testes de integração** — as rotas Flask e repositórios SQLite
   não têm testes automatizados; confiamos em testes manuais via browser.
2. **Sem CI/CD** — os testes rodam apenas localmente; um pipeline no GitHub
   Actions garantiria que nenhum commit quebra o build.
3. **Sem Docker** — a configuração do ambiente depende de instruções manuais
   no README; um `docker-compose.yml` simplificaria.
4. **Estimativas iniciais** — sem histórico de velocidade, a estimativa de
   43 SP foi um chute educado; funcionou, mas poderia ter sido mais precisa.

### Ações para próxima sprint 📝

| Ação | Responsável | Prioridade |
|---|---|---|
| Adicionar testes de integração para rotas | Equipe | Alta |
| Configurar GitHub Actions (CI) | Dev 2 | Média |
| Criar Dockerfile | Dev 3 | Baixa |
| Implementar edição/exclusão de transações (ICE-01) | Dev 1 | Média |
| Implementar alerta de limite mensal (ICE-04) | Dev 3 | Baixa |

---

## Resumo Executivo

A Sprint 1 foi concluída com **100% das user stories e tasks entregues**,
atingindo o Sprint Goal proposto. O produto FinTrack está funcional, testado
e documentado, pronto para a apresentação ao professor.

A equipe manteve foco na qualidade arquitetural (Clean Architecture + SOLID)
e na cobertura de testes (100% em domínio e use cases), conforme exigido
pela rubrica da atividade A2.

Os principais pontos de melhoria identificados (testes de integração, CI/CD,
Docker) foram registrados como ações para uma eventual Sprint 2.
