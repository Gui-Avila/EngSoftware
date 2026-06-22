# DIP: use cases dependem desta ABC, nunca da implementação concreta.
# ISP: só os métodos que os use cases consomem — buscar_por_id é
# necessário para validar categoria_id ao criar transação.

from abc import ABC, abstractmethod
from typing import Optional

from domain.entities.categoria import Categoria


class CategoriaRepository(ABC):
    """Contrato de persistência de categorias."""

    @abstractmethod
    def salvar(self, categoria: Categoria) -> None:
        """Persiste uma categoria."""

    @abstractmethod
    def buscar_por_id(self, categoria_id: str) -> Optional[Categoria]:
        """Retorna categoria pelo id, ou None se não existir."""

    @abstractmethod
    def listar(self) -> list[Categoria]:
        """Retorna todas as categorias."""
