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


    @property
    def limite(self) -> float:
        """
        Retorna o limite da conta corrente.

        """
        return self._limite
    

    def sacar(self, valor: float) -> None:
        """
        Realiza um saque na conta corrente, utilizando saldo + limite.

        :valor: Valor a ser sacado (deve ser maior que zero).
        :raises ValorInvalidoError: Se o valor for menor ou igual a zero.
        :raises SaldoInsuficienteError: Se o saldo + limite for insuficiente.
        """
        if valor <= 0:
            raise ValorInvalidoError(valor)

        saldo_disponivel: float = self._saldo + self._limite
        if valor > saldo_disponivel:
            raise SaldoInsuficienteError(saldo_disponivel, valor)

        self._saldo -= valor
        self._registrar(f"Saque (conta corrente) de R$ {valor:.2f}")

    def tipo_conta(self) -> str:
        """
        Retorna o nome do tipo de conta do cliente.

        """
        return "Conta Corrente"