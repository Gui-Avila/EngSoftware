from decimal import Decimal

import pytest

from domain.entities.transacao import TipoTransacao, Transacao
from domain.exceptions import DescricaoVaziaError, TipoInvalidoError, ValorInvalidoError


class TestTransacaoCriacaoValida:
    def test_cria_transacao_entrada(self):
        t = Transacao(
            descricao="Salário",
            valor=Decimal("5000"),
            tipo=TipoTransacao.ENTRADA,
            categoria_id="cat-1",
        )
        assert t.descricao == "Salário"
        assert t.valor == Decimal("5000")
        assert t.tipo == TipoTransacao.ENTRADA
        assert t.id is not None

    def test_cria_transacao_saida(self):
        t = Transacao(
            descricao="Aluguel",
            valor=Decimal("1500"),
            tipo=TipoTransacao.SAIDA,
            categoria_id="cat-2",
        )
        assert t.tipo == TipoTransacao.SAIDA

    def test_aceita_tipo_como_string(self):
        t = Transacao(
            descricao="Freelance",
            valor=Decimal("200"),
            tipo="ENTRADA",
            categoria_id="cat-1",
        )
        assert t.tipo == TipoTransacao.ENTRADA

    def test_converte_valor_numerico_para_decimal(self):
        t = Transacao(
            descricao="Café",
            valor=10,
            tipo=TipoTransacao.SAIDA,
            categoria_id="cat-1",
        )
        assert isinstance(t.valor, Decimal)
        assert t.valor == Decimal("10")


class TestTransacaoValorComSinal:
    def test_entrada_retorna_positivo(self):
        t = Transacao(
            descricao="Salário",
            valor=Decimal("3000"),
            tipo=TipoTransacao.ENTRADA,
            categoria_id="cat-1",
        )
        assert t.valor_com_sinal() == Decimal("3000")

    def test_saida_retorna_negativo(self):
        t = Transacao(
            descricao="Mercado",
            valor=Decimal("200"),
            tipo=TipoTransacao.SAIDA,
            categoria_id="cat-1",
        )
        assert t.valor_com_sinal() == Decimal("-200")


class TestTransacaoRegraDeNegocio:
    def test_valor_zero_lanca_excecao(self):
        with pytest.raises(ValorInvalidoError):
            Transacao(
                descricao="Nada",
                valor=Decimal("0"),
                tipo=TipoTransacao.ENTRADA,
                categoria_id="cat-1",
            )

    def test_valor_negativo_lanca_excecao(self):
        with pytest.raises(ValorInvalidoError):
            Transacao(
                descricao="Invalido",
                valor=Decimal("-50"),
                tipo=TipoTransacao.SAIDA,
                categoria_id="cat-1",
            )

    def test_descricao_vazia_lanca_excecao(self):
        with pytest.raises(DescricaoVaziaError):
            Transacao(
                descricao="",
                valor=Decimal("100"),
                tipo=TipoTransacao.ENTRADA,
                categoria_id="cat-1",
            )

    def test_descricao_so_espacos_lanca_excecao(self):
        with pytest.raises(DescricaoVaziaError):
            Transacao(
                descricao="   ",
                valor=Decimal("100"),
                tipo=TipoTransacao.ENTRADA,
                categoria_id="cat-1",
            )

    def test_tipo_invalido_lanca_excecao(self):
        with pytest.raises(TipoInvalidoError):
            Transacao(
                descricao="Teste",
                valor=Decimal("100"),
                tipo="TRANSFERENCIA",
                categoria_id="cat-1",
            )
