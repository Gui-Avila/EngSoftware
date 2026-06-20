from datetime import date
from decimal import Decimal

import pytest

from domain.entities.categoria import Categoria
from domain.entities.transacao import TipoTransacao
from domain.exceptions import CategoriaInexistenteError, ValorInvalidoError
from use_cases.criar_transacao import CriarTransacao


@pytest.fixture
def categoria_existente(categoria_repo):
    """Pré-cadastra uma categoria no fake para os testes."""
    cat = Categoria(nome="Salário")
    categoria_repo.salvar(cat)
    return cat


class TestCriarTransacao:
    def test_cria_transacao_entrada(
        self, transacao_repo, categoria_repo, categoria_existente
    ):
        uc = CriarTransacao(transacao_repo, categoria_repo)
        t = uc.executar(
            descricao="Salário mensal",
            valor=Decimal("5000"),
            tipo="ENTRADA",
            categoria_id=categoria_existente.id,
        )
        assert t.tipo == TipoTransacao.ENTRADA
        assert t.valor == Decimal("5000")

    def test_cria_transacao_saida(
        self, transacao_repo, categoria_repo, categoria_existente
    ):
        uc = CriarTransacao(transacao_repo, categoria_repo)
        t = uc.executar(
            descricao="Aluguel",
            valor=Decimal("1500"),
            tipo="SAIDA",
            categoria_id=categoria_existente.id,
        )
        assert t.tipo == TipoTransacao.SAIDA

    def test_transacao_com_data_especifica(
        self, transacao_repo, categoria_repo, categoria_existente
    ):
        uc = CriarTransacao(transacao_repo, categoria_repo)
        t = uc.executar(
            descricao="Bônus",
            valor=Decimal("1000"),
            tipo="ENTRADA",
            categoria_id=categoria_existente.id,
            data=date(2025, 1, 15),
        )
        assert t.data == date(2025, 1, 15)

    def test_categoria_inexistente_lanca_excecao(
        self, transacao_repo, categoria_repo
    ):
        uc = CriarTransacao(transacao_repo, categoria_repo)
        with pytest.raises(CategoriaInexistenteError):
            uc.executar(
                descricao="Teste",
                valor=Decimal("100"),
                tipo="ENTRADA",
                categoria_id="id-que-nao-existe",
            )

    def test_valor_negativo_lanca_excecao(
        self, transacao_repo, categoria_repo, categoria_existente
    ):
        uc = CriarTransacao(transacao_repo, categoria_repo)
        with pytest.raises(ValorInvalidoError):
            uc.executar(
                descricao="Invalido",
                valor=Decimal("-50"),
                tipo="SAIDA",
                categoria_id=categoria_existente.id,
            )

    def test_transacao_e_persistida(
        self, transacao_repo, categoria_repo, categoria_existente
    ):
        uc = CriarTransacao(transacao_repo, categoria_repo)
        uc.executar(
            descricao="Teste",
            valor=Decimal("100"),
            tipo="ENTRADA",
            categoria_id=categoria_existente.id,
        )
        assert len(transacao_repo.listar()) == 1
