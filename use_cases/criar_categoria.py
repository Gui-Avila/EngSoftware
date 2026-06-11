# Implementa HU-02: criar categorias para organizar transações.
# DIP: recebe CategoriaRepository (ABC) por injeção no construtor.

from decimal import Decimal
from typing import Optional

from domain.entities.categoria import Categoria
from use_cases.interfaces.categoria_repository import CategoriaRepository


class CriarCategoria:
    """Cria e persiste uma nova categoria."""

    def __init__(self, repo: CategoriaRepository):
        self._repo = repo

    def executar(self, nome: str, limite_mensal: Optional[Decimal] = None) -> Categoria:
        """Cria a categoria (validação fica na entidade) e salva via repositório."""
        categoria = Categoria(nome=nome, limite_mensal=limite_mensal)
        self._repo.salvar(categoria)
        return categoria
