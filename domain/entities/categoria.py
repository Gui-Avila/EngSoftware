from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from uuid import uuid4

from domain.exceptions import LimiteInvalidoError, NomeVazioError


@dataclass
class Categoria:
    """Categoria de transações financeiras.

    Regras de negócio:
    - nome não pode ser vazio
    - limite_mensal, se informado, deve ser >= 0
    """

    nome: str
    limite_mensal: Optional[Decimal] = None
    id: str = field(default_factory=lambda: str(uuid4()))

    def __post_init__(self):
        if not self.nome or not self.nome.strip():
            raise NomeVazioError("Nome da categoria não pode ser vazio.")

        if self.limite_mensal is not None:
            if not isinstance(self.limite_mensal, Decimal):
                self.limite_mensal = Decimal(str(self.limite_mensal))
            if self.limite_mensal < 0:
                raise LimiteInvalidoError("Limite mensal deve ser >= 0.")
