# Suporte a HU-01 e HU-03: listar transações cadastradas.
# DIP: depende da ABC TransacaoRepository.

from domain.entities.transacao import Transacao
from use_cases.interfaces.transacao_repository import TransacaoRepository


class ListarTransacoes:
    """Retorna todas as transações do repositório."""

    def __init__(self, repo: TransacaoRepository):
        self._repo = repo

    def executar(self) -> list[Transacao]:
        return self._repo.listar()
