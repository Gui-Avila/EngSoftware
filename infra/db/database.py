"""Inicialização do banco SQLite.

Camada externa (Frameworks & Drivers) — nenhuma regra de negócio aqui.
Só DDL e conexão.
"""

import sqlite3


def get_connection(db_path: str = "fintrack.db") -> sqlite3.Connection:
    """Retorna conexão SQLite com row_factory configurada."""
    conn = sqlite3.connect(db_path, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db(db_path: str = "fintrack.db") -> None:
    """Cria as tabelas se não existirem."""
    conn = get_connection(db_path)
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS categorias (
            id TEXT PRIMARY KEY,
            nome TEXT NOT NULL,
            limite_mensal TEXT
        );

        CREATE TABLE IF NOT EXISTS transacoes (
            id TEXT PRIMARY KEY,
            descricao TEXT NOT NULL,
            valor TEXT NOT NULL,
            tipo TEXT NOT NULL,
            data TEXT NOT NULL,
            categoria_id TEXT NOT NULL,
            FOREIGN KEY (categoria_id) REFERENCES categorias(id)
        );
    """)
    conn.commit()
    conn.close()
