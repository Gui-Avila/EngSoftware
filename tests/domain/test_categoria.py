from decimal import Decimal

import pytest

from domain.entities.categoria import Categoria
from domain.exceptions import LimiteInvalidoError, NomeVazioError


class TestCategoriaCriacaoValida:
    def test_cria_categoria_sem_limite(self):
        c = Categoria(nome="Alimentação")
        assert c.nome == "Alimentação"
        assert c.limite_mensal is None
        assert c.id is not None

    def test_cria_categoria_com_limite(self):
        c = Categoria(nome="Lazer", limite_mensal=Decimal("500"))
        assert c.limite_mensal == Decimal("500")

    def test_limite_zero_permitido(self):
        c = Categoria(nome="Reserva", limite_mensal=Decimal("0"))
        assert c.limite_mensal == Decimal("0")

    def test_converte_limite_numerico_para_decimal(self):
        c = Categoria(nome="Transporte", limite_mensal=300)
        assert isinstance(c.limite_mensal, Decimal)
        assert c.limite_mensal == Decimal("300")


class TestCategoriaRegraDeNegocio:
    def test_nome_vazio_lanca_excecao(self):
        with pytest.raises(NomeVazioError):
            Categoria(nome="")

    def test_nome_so_espacos_lanca_excecao(self):
        with pytest.raises(NomeVazioError):
            Categoria(nome="   ")

    def test_limite_negativo_lanca_excecao(self):
        with pytest.raises(LimiteInvalidoError):
            Categoria(nome="Teste", limite_mensal=Decimal("-100"))
