# Adapter de entrega web (HTML). Mesma camada que as rotas JSON —
# Interface Adapter na Clean Architecture. Só renderiza templates,
# sem regra de negócio.

from flask import Blueprint, render_template

frontend_bp = Blueprint(
    "frontend",
    __name__,
    template_folder="../templates",
    static_folder="../static",
)


@frontend_bp.route("/")
def index():
    return render_template("index.html", active="dashboard")


@frontend_bp.route("/ui/categorias")
def categorias():
    return render_template("categorias.html", active="categorias")


@frontend_bp.route("/ui/transacoes")
def transacoes():
    return render_template("transacoes.html", active="transacoes")
