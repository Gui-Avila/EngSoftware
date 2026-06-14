from decimal import Decimal

from domain.entities.transacao import TipoTransacao, Transacao
from use_cases.calcular_saldo import CalcularSaldo


class TestCalcularSaldo:
    def test_saldo_zero_sem_transacoes(self, transacao_repo):
        uc = CalcularSaldo(transacao_repo)
        assert uc.executar() == Decimal("0")

    def test_saldo_soma_entradas_subtrai_saidas(self, transacao_repo):
        transacao_repo.salvar(
            Transacao(
                descricao="Salário",
                valor=Decimal("5000"),
                tipo=TipoTransacao.ENTRADA,
                categoria_id="cat-1",
            )
        )
        transacao_repo.salvar(
            Transacao(
                descricao="Aluguel",
                valor=Decimal("1500"),
                tipo=TipoTransacao.SAIDA,
                categoria_id="cat-2",
            )
        )
        transacao_repo.salvar(
            Transacao(
                descricao="Mercado",
                valor=Decimal("500"),
                tipo=TipoTransacao.SAIDA,
                categoria_id="cat-2",
            )
        )
        uc = CalcularSaldo(transacao_repo)
        assert uc.executar() == Decimal("3000")

    def test_saldo_negativo_quando_saidas_maiores(self, transacao_repo):
        transacao_repo.salvar(
            Transacao(
                descricao="Entrada pequena",
                valor=Decimal("100"),
                tipo=TipoTransacao.ENTRADA,
                categoria_id="cat-1",
            )
        )
        transacao_repo.salvar(
            Transacao(
                descricao="Saída grande",
                valor=Decimal("500"),
                tipo=TipoTransacao.SAIDA,
                categoria_id="cat-2",
            )
        )
        uc = CalcularSaldo(transacao_repo)
        assert uc.executar() == Decimal("-400")

    def test_saldo_so_entradas(self, transacao_repo):
        transacao_repo.salvar(
            Transacao(
                descricao="Freelance",
                valor=Decimal("2000"),
                tipo=TipoTransacao.ENTRADA,
                categoria_id="cat-1",
            )
        )
        uc = CalcularSaldo(transacao_repo)
        assert uc.executar() == Decimal("2000")
