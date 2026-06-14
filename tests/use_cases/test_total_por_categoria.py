from decimal import Decimal

from domain.entities.categoria import Categoria
from domain.entities.transacao import TipoTransacao, Transacao
from use_cases.total_por_categoria import TotalPorCategoria


class TestTotalPorCategoria:
    def test_sem_categorias_retorna_lista_vazia(
        self, transacao_repo, categoria_repo
    ):
        uc = TotalPorCategoria(transacao_repo, categoria_repo)
        assert uc.executar() == []

    def test_categoria_sem_transacoes_retorna_zero(
        self, transacao_repo, categoria_repo
    ):
        cat = Categoria(nome="Alimentação")
        categoria_repo.salvar(cat)

        uc = TotalPorCategoria(transacao_repo, categoria_repo)
        resultado = uc.executar()

        assert len(resultado) == 1
        assert resultado[0].total == Decimal("0")
        assert resultado[0].nome == "Alimentação"

    def test_agrupa_corretamente_por_categoria(
        self, transacao_repo, categoria_repo
    ):
        alim = Categoria(nome="Alimentação")
        transp = Categoria(nome="Transporte")
        categoria_repo.salvar(alim)
        categoria_repo.salvar(transp)

        transacao_repo.salvar(
            Transacao(
                descricao="Mercado",
                valor=Decimal("200"),
                tipo=TipoTransacao.SAIDA,
                categoria_id=alim.id,
            )
        )
        transacao_repo.salvar(
            Transacao(
                descricao="Restaurante",
                valor=Decimal("80"),
                tipo=TipoTransacao.SAIDA,
                categoria_id=alim.id,
            )
        )
        transacao_repo.salvar(
            Transacao(
                descricao="Uber",
                valor=Decimal("50"),
                tipo=TipoTransacao.SAIDA,
                categoria_id=transp.id,
            )
        )

        uc = TotalPorCategoria(transacao_repo, categoria_repo)
        resultado = uc.executar()
        por_nome = {r.nome: r.total for r in resultado}

        assert por_nome["Alimentação"] == Decimal("-280")
        assert por_nome["Transporte"] == Decimal("-50")

    def test_mistura_entradas_e_saidas_na_mesma_categoria(
        self, transacao_repo, categoria_repo
    ):
        cat = Categoria(nome="Freelance")
        categoria_repo.salvar(cat)

        transacao_repo.salvar(
            Transacao(
                descricao="Recebimento",
                valor=Decimal("1000"),
                tipo=TipoTransacao.ENTRADA,
                categoria_id=cat.id,
            )
        )
        transacao_repo.salvar(
            Transacao(
                descricao="Material",
                valor=Decimal("300"),
                tipo=TipoTransacao.SAIDA,
                categoria_id=cat.id,
            )
        )

        uc = TotalPorCategoria(transacao_repo, categoria_repo)
        resultado = uc.executar()

        assert len(resultado) == 1
        assert resultado[0].total == Decimal("700")
