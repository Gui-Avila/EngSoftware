from decimal import Decimal

import pytest

from domain.exceptions import NomeVazioError
from use_cases.criar_categoria import CriarCategoria


class TestCriarCategoria:
    def test_cria_categoria_com_sucesso(self, categoria_repo):
        uc = CriarCategoria(categoria_repo)
        cat = uc.executar(nome="Alimentação")

        assert cat.nome == "Alimentação"
        assert cat.id is not None
        assert categoria_repo.buscar_por_id(cat.id) is not None

    def test_cria_categoria_com_limite(self, categoria_repo):
        uc = CriarCategoria(categoria_repo)
        cat = uc.executar(nome="Lazer", limite_mensal=Decimal("500"))

        assert cat.limite_mensal == Decimal("500")

    def test_nome_vazio_lanca_excecao(self, categoria_repo):
        uc = CriarCategoria(categoria_repo)
        with pytest.raises(NomeVazioError):
            uc.executar(nome="")

    def test_categoria_e_persistida_no_repositorio(self, categoria_repo):
        uc = CriarCategoria(categoria_repo)
        cat = uc.executar(nome="Transporte")

        todas = categoria_repo.listar()
        assert len(todas) == 1
        assert todas[0].id == cat.id
