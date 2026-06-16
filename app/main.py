# Wiring: único ponto que conhece tanto as ABCs quanto as implementações
# concretas. Aqui a inversão de dependência é amarrada — os use cases
# recebem os repositórios por injeção no construtor.

from flask import Flask

from infra.db.database import get_connection, init_db
from infra.repositories.categoria_repository_sqlite import CategoriaRepositorySQLite
from infra.repositories.transacao_repository_sqlite import TransacaoRepositorySQLite
from use_cases.calcular_saldo import CalcularSaldo
from use_cases.criar_categoria import CriarCategoria
from use_cases.criar_transacao import CriarTransacao
from use_cases.listar_transacoes import ListarTransacoes
from use_cases.total_por_categoria import TotalPorCategoria


def create_app(db_path: str = "fintrack.db") -> Flask:
    """Factory da aplicação Flask com injeção de dependências."""
    app = Flask(__name__)

    init_db(db_path)
    conn = get_connection(db_path)

    categoria_repo = CategoriaRepositorySQLite(conn)
    transacao_repo = TransacaoRepositorySQLite(conn)

    app.config["use_cases"] = {
        "criar_categoria": CriarCategoria(categoria_repo),
        "criar_transacao": CriarTransacao(transacao_repo, categoria_repo),
        "listar_transacoes": ListarTransacoes(transacao_repo),
        "calcular_saldo": CalcularSaldo(transacao_repo),
        "total_por_categoria": TotalPorCategoria(transacao_repo, categoria_repo),
        "categoria_repo": categoria_repo,
    }

    from app.routes.categoria_routes import categoria_bp
    from app.routes.frontend_routes import frontend_bp
    from app.routes.transacao_routes import transacao_bp

    app.register_blueprint(categoria_bp)
    app.register_blueprint(transacao_bp)
    app.register_blueprint(frontend_bp)

    return app
