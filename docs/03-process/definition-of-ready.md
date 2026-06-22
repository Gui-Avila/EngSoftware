# Definition of Ready (DoR) — FinTrack

Uma história só entra na sprint quando todos os critérios abaixo são atendidos.
O objetivo é evitar que itens mal definidos gerem retrabalho durante a
execução.

A estrutura segue o acrônimo **INVEST**:

## Checklist

- [ ] **Independent** — a história pode ser desenvolvida sem depender de outra
  história que ainda não foi concluída na mesma sprint. Se há dependência,
  está explicitamente declarada e a história dependida está priorizada antes.
- [ ] **Negotiable** — a história descreve *o que* o usuário precisa, não *como*
  implementar. Detalhes técnicos ficam a critério do time.
- [ ] **Valuable** — a história entrega valor perceptível ao usuário final ou
  viabiliza uma feature que entrega (caso de enabler).
- [ ] **Estimable** — o time conseguiu estimar em Story Points. Se houve
  incerteza, uma spike foi feita antes.
- [ ] **Small** — a história cabe em uma sprint. Se for grande demais, foi
  quebrada em histórias menores.
- [ ] **Testable** — os critérios de aceitação estão escritos em formato BDD
  (Dado/Quando/Então) e são verificáveis por teste automatizado ou manual.

## Critérios específicos deste projeto

- [ ] Narrativa no formato "Como \<persona\> quero \<ação\> para \<benefício\>"
- [ ] Persona declarada e presente em `docs/01-product/personas.md`
- [ ] Mínimo de 3 critérios de aceitação em formato BDD
- [ ] Story Points atribuídos (escala Fibonacci: 1, 2, 3, 5, 8, 13)
- [ ] Dependências mapeadas (outras histórias, enablers, dados de teste)
- [ ] Regras de negócio listadas e sem ambiguidade
- [ ] Camada de destino identificada (entidade, use case, rota)
