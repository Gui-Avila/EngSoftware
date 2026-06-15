# Adapter (GoF): adapta SQLite à interface CategoriaRepository.
# LSP: intercambiável com qualquer outra implementação da ABC
# sem o use case perceber.

import sqlite3
from decimal import Decimal

from domain.entities.categoria import Categoria
from use_cases.interfaces.categoria_repository import CategoriaRepository


class CategoriaRepositorySQLite(CategoriaRepository):
    """Implementação concreta com SQLite."""

    def __init__(self, conn: sqlite3.Connection):
        self._conn = conn

    def salvar(self, categoria: Categoria) -> None:
        limite = str(categoria.limite_mensal) if categoria.limite_mensal is not None else None
        self._conn.execute(
            "INSERT INTO categorias (id, nome, limite_mensal) VALUES (?, ?, ?)",
            (categoria.id, categoria.nome, limite),
        )
        self._conn.commit()

    def buscar_por_id(self, categoria_id: str) -> Categoria | None:
        row = self._conn.execute(
            "SELECT id, nome, limite_mensal FROM categorias WHERE id = ?",
            (categoria_id,),
        ).fetchone()

        if row is None:
            return None

        return self._row_para_categoria(row)

    def listar(self) -> list[Categoria]:
        rows = self._conn.execute(
            "SELECT id, nome, limite_mensal FROM categorias"
        ).fetchall()
        return [self._row_para_categoria(r) for r in rows]

    @staticmethod
    def _row_para_categoria(row: sqlite3.Row) -> Categoria:
        limite = Decimal(row["limite_mensal"]) if row["limite_mensal"] is not None else None
        return Categoria(
            nome=row["nome"],
            limite_mensal=limite,
            id=row["id"],
        )
