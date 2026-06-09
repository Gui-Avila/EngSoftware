# SRP: a entidade Transacao contém apenas regras de negócio.
# Quem persiste é o repositório (separação entidade/persistência,
# como o exemplo Animal/AnimalDAO do material).

from dataclasses import dataclass, field
from datetime import date
from decimal import Decimal
from enum import Enum
from uuid import uuid4

from domain.exceptions import DescricaoVaziaError, TipoInvalidoError, ValorInvalidoError


class TipoTransacao(Enum):
    """Tipo de movimentação financeira."""

    ENTRADA = "ENTRADA"
    SAIDA = "SAIDA"


@dataclass
class Transacao:
    """Transação financeira (entrada ou saída).

    Regras de negócio:
    - valor deve ser > 0 (armazenado sempre positivo)
    - tipo deve ser ENTRADA ou SAIDA
    - descrição não pode ser vazia
    """

    descricao: str
    valor: Decimal
    tipo: TipoTransacao
    categoria_id: str
    data: date = field(default_factory=date.today)
    id: str = field(default_factory=lambda: str(uuid4()))

    def __post_init__(self):
        if not self.descricao or not self.descricao.strip():
            raise DescricaoVaziaError("Descrição não pode ser vazia.")

        if not isinstance(self.valor, Decimal):
            self.valor = Decimal(str(self.valor))

        if self.valor <= 0:
            raise ValorInvalidoError("Valor deve ser maior que zero.")

        if not isinstance(self.tipo, TipoTransacao):
            try:
                self.tipo = TipoTransacao(self.tipo)
            except ValueError:
                raise TipoInvalidoError(
                    f"Tipo inválido: {self.tipo}. Use ENTRADA ou SAIDA."
                )

    def valor_com_sinal(self) -> Decimal:
        """Retorna +valor para ENTRADA, -valor para SAIDA."""
        if self.tipo == TipoTransacao.ENTRADA:
            return self.valor
        return -self.valor
