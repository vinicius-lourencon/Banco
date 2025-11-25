class ErroBanco(Exception):
    """
    Exceção base para erros específicos do sistema bancário.

    Todas as outras exceções personalizadas vão herdar desta classe.
    """

    def __init__(self, mensagem: str) -> None:
        """
        Inicializa a exceção com uma mensagem descritiva.

        mensagem: Texto explicando o erro ocorrido.
        """
        super().__init__(mensagem)
