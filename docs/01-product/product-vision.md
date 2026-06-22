# Visão do Produto — FinTrack

## Declaração de Visão (template Geoffrey Moore)

> **Para** pessoas que controlam suas finanças pessoais manualmente ou em
> planilhas desorganizadas,
>
> **Que** perdem visibilidade de para onde o dinheiro vai e frequentemente
> chegam ao fim do mês sem saber por que o saldo está negativo,
>
> **O FinTrack** é um gerenciador financeiro pessoal web
>
> **Que** permite registrar transações de entrada e saída, categorizá-las e
> consultar saldo e relatórios por categoria em tempo real,
>
> **Diferentemente de** planilhas manuais ou aplicativos bancários que
> mostram extrato bruto sem categorização flexível,
>
> **Nosso produto** oferece organização por categorias definidas pelo usuário,
> cálculo automático de saldo e visão consolidada de gastos por categoria,
> tudo em uma interface web acessível via navegador.

## Objetivos do Produto

| Objetivo | KPI |
|---|---|
| Registrar movimentações financeiras com classificação | 100% das transações vinculadas a uma categoria |
| Fornecer saldo atualizado | Saldo recalculado a cada consulta com base em todas as transações |
| Visibilidade de gastos por categoria | Relatório por categoria disponível via endpoint e dashboard |
| Manter integridade dos dados | Validações de domínio impedem transações com valor ≤ 0, descrição vazia ou categoria inexistente |

## Escopo

### O que é

- Aplicação web (Flask) para registro e consulta de finanças pessoais.
- Duas entidades de domínio: Transação e Categoria.
- Cinco casos de uso: criar transação, criar categoria, listar transações,
  calcular saldo, total por categoria.
- Persistência em SQLite.
- Interface web com dashboard, página de categorias e página de transações.

### O que não é

- Não é multi-usuário (sem autenticação).
- Não é aplicativo mobile.
- Não importa extratos bancários.
- Não faz projeções, orçamentos ou alertas de limite.
- Não implementa edição nem exclusão de registros.
