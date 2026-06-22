"""Fakes in-memory dos repositórios para testes de use case.

Implementam as mesmas ABCs que os repositórios SQLite, provando o DIP:
o use case roda igual com fake ou com banco real, sem mudar uma linha.
"""

from typing import Optional

import pytest

from domain.entities.categoria import Categoria
from domain.entities.transacao import Transacao
from use_cases.interfaces.categoria_repository import CategoriaRepository
from use_cases.interfaces.transacao_repository import TransacaoRepository


class FakeTransacaoRepository(TransacaoRepository):
    """Repositório em memória para testes. LSP: intercambiável com o SQLite."""

    def __init__(self):
        self._transacoes: list[Transacao] = []

    def salvar(self, transacao: Transacao) -> None:
        self._transacoes.append(transacao)

    def listar(self) -> list[Transacao]:
        return list(self._transacoes)

    def listar_por_categoria(self, categoria_id: str) -> list[Transacao]:
        return [t for t in self._transacoes if t.categoria_id == categoria_id]


class FakeCategoriaRepository(CategoriaRepository):
    """Repositório em memória para testes. LSP: intercambiável com o SQLite."""

    def __init__(self):
        self._categorias: dict[str, Categoria] = {}

    def salvar(self, categoria: Categoria) -> None:
        self._categorias[categoria.id] = categoria

    def buscar_por_id(self, categoria_id: str) -> Optional[Categoria]:
        return self._categorias.get(categoria_id)

    def listar(self) -> list[Categoria]:
        return list(self._categorias.values())


@pytest.fixture
def transacao_repo():
    return FakeTransacaoRepository()


@pytest.fixture
def categoria_repo():
    return FakeCategoriaRepository()
