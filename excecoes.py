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

class SaldoInsuficienteError(ErroBanco):
    """
    Exceção lançada quando o saldo (mais limite, se houver)
    não é suficiente para concluir uma operação de saque ou débito.
    """

    def __init__(self, saldo_atual: float, valor: float) -> None:
        """
        Cria uma exceção com detalhes do saldo e valor da tentativa.

        :saldo_atual: Valor disponível (saldo ou saldo + limite).
        :valor: Valor que se tentou sacar/debitar.
        """
        mensagem = (
            f"Saldo insuficiente. Saldo disponível: {saldo_atual:.2f}, "
            f"tentativa de saque: {valor:.2f}."
        )
        super().__init__(mensagem)

