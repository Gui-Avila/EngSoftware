# Adapter de entrega: converte HTTP (JSON) <-> use cases.
# Nenhuma regra de negócio aqui — só orquestração.

from decimal import Decimal, InvalidOperation

from flask import Blueprint, current_app, jsonify, request

from domain.exceptions import DominioError

categoria_bp = Blueprint("categorias", __name__)


@categoria_bp.route("/categorias", methods=["POST"])
def criar_categoria():
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "Corpo JSON ausente."}), 400

    limite = dados.get("limite_mensal")
    if limite is not None:
        try:
            limite = Decimal(str(limite))
        except InvalidOperation:
            return jsonify({"erro": "limite_mensal inválido."}), 422

    try:
        uc = current_app.config["use_cases"]["criar_categoria"]
        cat = uc.executar(nome=dados.get("nome", ""), limite_mensal=limite)
    except DominioError as e:
        return jsonify({"erro": str(e)}), 422

    return jsonify({
        "id": cat.id,
        "nome": cat.nome,
        "limite_mensal": str(cat.limite_mensal) if cat.limite_mensal is not None else None,
    }), 201


@categoria_bp.route("/categorias", methods=["GET"])
def listar_categorias():
    repo = current_app.config["use_cases"]["categoria_repo"]
    categorias = repo.listar()
    return jsonify([
        {
            "id": c.id,
            "nome": c.nome,
            "limite_mensal": str(c.limite_mensal) if c.limite_mensal is not None else None,
        }
        for c in categorias
    ])
