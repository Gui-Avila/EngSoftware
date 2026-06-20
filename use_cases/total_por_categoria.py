# Implementa HU-04: ver total gasto/recebido por categoria.
# DIP: depende das ABCs TransacaoRepository e CategoriaRepository.

from dataclasses import dataclass
from decimal import Decimal

from use_cases.interfaces.categoria_repository import CategoriaRepository
from use_cases.interfaces.transacao_repository import TransacaoRepository


@dataclass
class TotalCategoria:
    """Resultado agregado: total com sinal por categoria."""

    categoria_id: str
    nome: str
    total: Decimal


class TotalPorCategoria:
    """Agrupa transações por categoria e soma valor_com_sinal."""

    def __init__(
        self,
        transacao_repo: TransacaoRepository,
        categoria_repo: CategoriaRepository,
    ):
        self._transacao_repo = transacao_repo
        self._categoria_repo = categoria_repo

    def executar(self) -> list[TotalCategoria]:
        categorias = self._categoria_repo.listar()
        resultado = []

        for cat in categorias:
            transacoes = self._transacao_repo.listar_por_categoria(cat.id)
            total = sum(
                (t.valor_com_sinal() for t in transacoes),
                Decimal("0"),
            )
            resultado.append(
                TotalCategoria(categoria_id=cat.id, nome=cat.nome, total=total)
            )

        return resultado
