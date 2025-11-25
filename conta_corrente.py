from conta import Conta
from cliente import Cliente
from excecoes import ValorInvalidoError, SaldoInsuficienteError

class ContaCorrente(Conta):
    """
    Representa uma conta corrente.

    Permite utilização de um limite adicional (cheque especial).
    """

    def __init__(
        self,
        numero: str,
        cliente: Cliente,
        saldo_inicial: float = 0.0,
        limite: float = 0.0,
    ) -> None:
        """
        Inicializa uma conta corrente com limite.

        :numero: Número identificador da conta.
        :cliente: Cliente associado à conta.
        :saldo_inicial: Saldo inicial da conta.
        :limite: Limite adicional disponível para saques.
        """
        super().__init__(numero, cliente, saldo_inicial)
        self._limite: float = float(limite)

