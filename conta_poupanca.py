from conta import Conta


class ContaPoupanca(Conta):
    """
    Representa uma conta poupança, sem limites.

    Neste protótipo, não há cálculo de rendimento automático.
    """

    def tipo_conta(self) -> str:
        """
        Retorna o nome do tipo de conta.

        :return: String 'Conta Poupança'.
        """
        return "Conta Poupança"