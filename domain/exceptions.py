"""Exceções de domínio do FinTrack.

Cada exceção representa uma violação de regra de negócio. Ficam na camada
de domínio porque são parte do vocabulário do negócio, não de infraestrutura.
"""


class DominioError(Exception):
    """Classe-base para erros de domínio."""


class ValorInvalidoError(DominioError):
    """Valor da transação deve ser positivo (> 0)."""


class DescricaoVaziaError(DominioError):
    """Descrição da transação não pode ser vazia."""


class TipoInvalidoError(DominioError):
    """Tipo da transação deve ser ENTRADA ou SAIDA."""


class NomeVazioError(DominioError):
    """Nome da categoria não pode ser vazio."""


class LimiteInvalidoError(DominioError):
    """Limite mensal, se informado, deve ser >= 0."""


class CategoriaInexistenteError(DominioError):
    """Categoria referenciada não existe no repositório."""
