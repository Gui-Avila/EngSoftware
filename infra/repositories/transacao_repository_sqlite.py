# Adapter (GoF): adapta SQLite à interface TransacaoRepository.
# LSP: intercambiável com qualquer outra implementação da ABC.

import sqlite3
from datetime import date
from decimal import Decimal

from domain.entities.transacao import TipoTransacao, Transacao
from use_cases.interfaces.transacao_repository import TransacaoRepository


class TransacaoRepositorySQLite(TransacaoRepository):
    """Implementação concreta com SQLite."""

    def __init__(self, conn: sqlite3.Connection):
        self._conn = conn

    def salvar(self, transacao: Transacao) -> None:
        self._conn.execute(
            "INSERT INTO transacoes (id, descricao, valor, tipo, data, categoria_id) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            (
                transacao.id,
                transacao.descricao,
                str(transacao.valor),
                transacao.tipo.value,
                transacao.data.isoformat(),
                transacao.categoria_id,
            ),
        )
        self._conn.commit()

    def listar(self) -> list[Transacao]:
        rows = self._conn.execute(
            "SELECT id, descricao, valor, tipo, data, categoria_id FROM transacoes"
        ).fetchall()
        return [self._row_para_transacao(r) for r in rows]

    def listar_por_categoria(self, categoria_id: str) -> list[Transacao]:
        rows = self._conn.execute(
            "SELECT id, descricao, valor, tipo, data, categoria_id "
            "FROM transacoes WHERE categoria_id = ?",
            (categoria_id,),
        ).fetchall()
        return [self._row_para_transacao(r) for r in rows]

    @staticmethod
    def _row_para_transacao(row: sqlite3.Row) -> Transacao:
        return Transacao(
            descricao=row["descricao"],
            valor=Decimal(row["valor"]),
            tipo=TipoTransacao(row["tipo"]),
            categoria_id=row["categoria_id"],
            data=date.fromisoformat(row["data"]),
            id=row["id"],
        )
