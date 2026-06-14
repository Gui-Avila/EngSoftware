# Implementa HU-03: consultar saldo atual (entradas - saídas).
# DIP: depende da ABC TransacaoRepository.

from decimal import Decimal

from use_cases.interfaces.transacao_repository import TransacaoRepository


class CalcularSaldo:
    """Soma valor_com_sinal() de todas as transações."""

    def __init__(self, repo: TransacaoRepository):
        self._repo = repo

    def executar(self) -> Decimal:
        transacoes = self._repo.listar()
        return sum(
            (t.valor_com_sinal() for t in transacoes),
            Decimal("0"),
        )
