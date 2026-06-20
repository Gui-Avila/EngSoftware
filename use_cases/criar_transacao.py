# Implementa HU-01: registrar transação (entrada ou saída).
# DIP: recebe as ABCs dos dois repositórios por injeção.

from datetime import date
from decimal import Decimal
from typing import Optional

from domain.entities.transacao import TipoTransacao, Transacao
from domain.exceptions import CategoriaInexistenteError
from use_cases.interfaces.categoria_repository import CategoriaRepository
from use_cases.interfaces.transacao_repository import TransacaoRepository


class CriarTransacao:
    """Valida categoria, cria e persiste uma transação."""

    def __init__(
        self,
        transacao_repo: TransacaoRepository,
        categoria_repo: CategoriaRepository,
    ):
        self._transacao_repo = transacao_repo
        self._categoria_repo = categoria_repo

    def executar(
        self,
        descricao: str,
        valor: Decimal,
        tipo: str | TipoTransacao,
        categoria_id: str,
        data: Optional[date] = None,
    ) -> Transacao:
        """Cria transação após verificar que a categoria existe."""
        categoria = self._categoria_repo.buscar_por_id(categoria_id)
        if categoria is None:
            raise CategoriaInexistenteError(
                f"Categoria '{categoria_id}' não encontrada."
            )

        kwargs = {
            "descricao": descricao,
            "valor": valor,
            "tipo": tipo,
            "categoria_id": categoria_id,
        }
        if data is not None:
            kwargs["data"] = data

        transacao = Transacao(**kwargs)
        self._transacao_repo.salvar(transacao)
        return transacao
