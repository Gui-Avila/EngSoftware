# Definition of Done (DoD) — FinTrack

Uma história é considerada **Done** quando todos os critérios abaixo são
atendidos. O DoD é cumulativo: itens de qualidade e NFRs se somam aos
critérios funcionais.

## Funcional

- [ ] Todos os critérios de aceitação (BDD) da história foram atendidos
- [ ] Endpoint(s) correspondente(s) implementados e respondendo com os
  códigos HTTP corretos (201 para criação, 200 para consulta, 4xx para erros)
- [ ] Valores monetários serializados como string decimal no JSON
  (preservação de `Decimal`)
- [ ] Dados persistidos no banco SQLite via repositório

## Qualidade de código

- [ ] Código segue PEP-8 — `ruff check .` retorna zero erros
- [ ] Use case depende apenas de ABCs declaradas em `use_cases/interfaces/`,
  nunca de implementações concretas
- [ ] Rota Flask faz apenas parsing de request e formatação de response —
  lógica de negócio delegada ao use case
- [ ] Exceções de domínio são específicas e descritivas (hierarquia sob
  `DominioError`)
- [ ] Código commitado com mensagem descritiva

## NFR — Manutenibilidade

Critério: o código pode ser estendido ou ter componentes substituídos sem
alterar as camadas internas.

- [ ] Entidades são objetos Python puros — sem imports de Flask, SQLite ou
  qualquer framework
- [ ] Use cases importam apenas de `domain/` e `use_cases/interfaces/` —
  verificável por inspeção dos imports
- [ ] Repositórios SQLite implementam as mesmas ABCs que os fakes de teste
  (LSP) — trocar banco não exige alterar use case
- [ ] Princípios SOLID aplicados:
  - SRP: cada classe tem uma única responsabilidade
  - OCP: novo repositório ou use case não exige alterar código existente
  - LSP: fakes e SQLite repos intercambiáveis via interface
  - ISP: ABCs de repositório expõem apenas os métodos que os use cases
    consomem
  - DIP: use cases dependem de abstrações, não de implementações

## NFR — Testabilidade

Critério: use cases podem ser testados isoladamente, sem banco de dados,
rede ou framework web.

- [ ] Testes unitários escritos para o use case com fakes in-memory que
  implementam as mesmas ABCs dos repositórios reais
- [ ] Testes cobrem caminho feliz e ao menos uma violação de regra de negócio
- [ ] Cobertura de `domain/` + `use_cases/` ≥ 80% (threshold configurado em
  `pyproject.toml`)
- [ ] `pytest` executa todos os testes em menos de 5 segundos sem
  dependência de infraestrutura externa
- [ ] Cobertura real verificada: 144/144 statements, 100%
  (`pytest --cov --cov-report=term-missing`)

## Documentação

- [ ] História documentada em `docs/02-backlog/user-stories/` com
  rastreabilidade para o código
- [ ] README do projeto atualizado se houver mudança em endpoints ou setup
