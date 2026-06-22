# Matriz de Story Points — FinTrack

## Escala de referência (Fibonacci)

| SP | Esforço | Tempo estimado | Complexidade | Risco |
|---|---|---|---|---|
| 1 | Trivial — alteração pontual | < 2h | Nenhuma lógica condicional | Nenhum |
| 2 | Baixo — implementação direta | 2–4h | Lógica linear, sem interações entre componentes | Mínimo |
| 3 | Moderado — mais de um componente | 4–8h | Validações ou transformações simples | Baixo |
| 5 | Significativo — múltiplas camadas | 1–2 dias | Interação entre entidades/repos, múltiplas exceções | Médio |
| 8 | Alto — feature completa cross-cutting | 2–3 dias | Orquestração complexa, múltiplas dependências | Médio-alto |
| 13 | Muito alto — considerar quebrar | > 3 dias | Incerteza técnica, prototipação necessária | Alto |

A estimativa considera quatro fatores com pesos iguais: esforço de
implementação, tempo necessário, complexidade da lógica e risco de
impedimentos ou retrabalho.

## Aplicação às histórias do FinTrack

| ID | Título | SP | Justificativa |
|---|---|---|---|
| US-01 | Registrar transação financeira | 5 | Envolve duas entidades (`Transacao` + validação de `Categoria`), dois repositórios injetados, cinco validações de domínio com exceções distintas, parsing de data opcional na rota. Dependência de US-02 adiciona risco de integração. |
| US-02 | Criar categoria | 3 | Uma entidade com duas validações simples (nome vazio, limite negativo), um repositório, um use case direto. Sem dependências externas. O endpoint de listagem (`GET /categorias`) é leitura pura. |
| US-03 | Consultar saldo | 3 | Dois use cases (`CalcularSaldo`, `ListarTransacoes`), mas lógica simples: soma aritmética com `valor_com_sinal()`. Sem escrita no banco, sem validações de input. A complexidade está na cobertura de cenários (zero, negativo, misto), não na implementação. |
| US-04 | Totais por categoria | 5 | Agregação cross-entity: itera categorias, busca transações de cada uma, soma valores com sinal. Requer `listar_por_categoria()` no repo (método adicional na ABC). Dataclass de resultado (`TotalCategoria`). Mais caminhos a testar (sem categorias, sem transações, misto). |

### Resumo

| | US-01 | US-02 | US-03 | US-04 | Total |
|---|---|---|---|---|---|
| **SP** | 5 | 3 | 3 | 5 | **16** |
