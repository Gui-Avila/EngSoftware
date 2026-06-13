from decimal import Decimal

from domain.entities.transacao import TipoTransacao, Transacao
from use_cases.listar_transacoes import ListarTransacoes


class TestListarTransacoes:
    def test_lista_vazia_sem_transacoes(self, transacao_repo):
        uc = ListarTransacoes(transacao_repo)
        assert uc.executar() == []

    def test_lista_transacoes_cadastradas(self, transacao_repo):
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
        uc = ListarTransacoes(transacao_repo)
        resultado = uc.executar()
        assert len(resultado) == 2

    def test_retorna_copia_da_lista(self, transacao_repo):
        """Garante que o retorno não é referência interna do repo."""
        transacao_repo.salvar(
            Transacao(
                descricao="Teste",
                valor=Decimal("100"),
                tipo=TipoTransacao.ENTRADA,
                categoria_id="cat-1",
            )
        )
        uc = ListarTransacoes(transacao_repo)
        lista = uc.executar()
        lista.clear()
        assert len(uc.executar()) == 1
