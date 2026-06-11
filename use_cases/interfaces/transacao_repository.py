# DIP: use cases dependem desta ABC, nunca da implementação concreta.
# ISP: interface enxuta — só os métodos que os use cases precisam.
# Não tem delete/update porque nenhum use case pede isso.

from abc import ABC, abstractmethod

from domain.entities.transacao import Transacao


class TransacaoRepository(ABC):
    """Contrato de persistência de transações."""

    @abstractmethod
    def salvar(self, transacao: Transacao) -> None:
        """Persiste uma transação."""

    @abstractmethod
    def listar(self) -> list[Transacao]:
        """Retorna todas as transações."""

    @abstractmethod
    def listar_por_categoria(self, categoria_id: str) -> list[Transacao]:
        """Retorna transações de uma categoria específica."""
