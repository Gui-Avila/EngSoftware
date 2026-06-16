# Adapter de entrega: converte HTTP (JSON) <-> use cases.
# Nenhuma regra de negócio aqui — só orquestração.

from datetime import date
from decimal import Decimal, InvalidOperation

from flask import Blueprint, current_app, jsonify, request

from domain.exceptions import CategoriaInexistenteError, DominioError

transacao_bp = Blueprint("transacoes", __name__)


def _transacao_para_dict(t):
    return {
        "id": t.id,
        "descricao": t.descricao,
        "valor": str(t.valor),
        "tipo": t.tipo.value,
        "data": t.data.isoformat(),
        "categoria_id": t.categoria_id,
    }


@transacao_bp.route("/transacoes", methods=["POST"])
def criar_transacao():
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "Corpo JSON ausente."}), 400

    try:
        valor = Decimal(str(dados.get("valor", "")))
    except InvalidOperation:
        return jsonify({"erro": "Valor inválido."}), 422

    data_str = dados.get("data")
    data = date.fromisoformat(data_str) if data_str else None

    try:
        uc = current_app.config["use_cases"]["criar_transacao"]
        t = uc.executar(
            descricao=dados.get("descricao", ""),
            valor=valor,
            tipo=dados.get("tipo", ""),
            categoria_id=dados.get("categoria_id", ""),
            data=data,
        )
    except CategoriaInexistenteError as e:
        return jsonify({"erro": str(e)}), 404
    except DominioError as e:
        return jsonify({"erro": str(e)}), 422

    return jsonify(_transacao_para_dict(t)), 201


@transacao_bp.route("/transacoes", methods=["GET"])
def listar_transacoes():
    uc = current_app.config["use_cases"]["listar_transacoes"]
    transacoes = uc.executar()
    return jsonify([_transacao_para_dict(t) for t in transacoes])


@transacao_bp.route("/saldo", methods=["GET"])
def consultar_saldo():
    uc = current_app.config["use_cases"]["calcular_saldo"]
    saldo = uc.executar()
    return jsonify({"saldo": str(saldo)})


@transacao_bp.route("/relatorios/por-categoria", methods=["GET"])
def total_por_categoria():
    uc = current_app.config["use_cases"]["total_por_categoria"]
    resultado = uc.executar()
    return jsonify({
        "categorias": [
            {
                "categoria_id": r.categoria_id,
                "nome": r.nome,
                "total": str(r.total),
            }
            for r in resultado
        ]
    })
