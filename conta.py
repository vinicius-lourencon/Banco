from abc import ABC, abstractmethod
from typing import List

from cliente import Cliente
from excecoes import ValorInvalidoError, SaldoInsuficienteError


class Conta(ABC):
    """
    Classe base abstrata para contas bancárias.

    Fornece operações comuns como depósito, saque e geração de extrato.
    """

    def __init__(self, numero: str, cliente: Cliente, saldo_inicial: float = 0.0) -> None:
        """
        Inicializa uma nova conta bancária.

        :param numero: Número identificador da conta.
        :param cliente: Cliente associado a esta conta.
        :param saldo_inicial: Saldo inicial da conta (padrão: 0.0).
        """
        self._numero: str = numero
        self._cliente: Cliente = cliente
        self._saldo: float = float(saldo_inicial)
        self._historico: List[str] = []
        

    @property
    def numero(self) -> str:
        """
        Retorna o número identificador da conta.

        :return: Número da conta.
        """
        return self._numero

    @property
    def cliente(self) -> Cliente:
        """
        Retorna o cliente associado à conta.

        """
        return self._cliente

    @property
    def saldo(self) -> float:
        """
        Retorna o saldo atual da conta.

        """
        return self._saldo

    def _registrar(self, mensagem: str) -> None:
        """
        Registra uma mensagem no histórico da conta.

        :mensagem: Texto descrevendo a movimentação realizada.
        """
        self._historico.append(mensagem)

    def depositar(self, valor: float) -> None:
        """
        Realiza um depósito na conta, caso o valor seja válido.

        :valor: Valor a ser depositado (deve ser maior que zero).
        :raises ValorInvalidoError: Se o valor for menor ou igual a zero.
        """
        if valor <= 0:
            raise ValorInvalidoError(valor)
        self._saldo += valor
        self._registrar(f"Depósito de R$ {valor:.2f}")

    def sacar(self, valor: float) -> None:
        """
        Realiza um saque na conta, caso haja saldo suficiente.

        :valor: Valor a ser sacado (deve ser maior que zero).
        :raises ValorInvalidoError: Se o valor for menor ou igual a zero.
        :raises SaldoInsuficienteError: Se o saldo for insuficiente.
        """
        if valor <= 0:
            raise ValorInvalidoError(valor)
        if valor > self._saldo:
            raise SaldoInsuficienteError(self._saldo, valor)
        self._saldo -= valor
        self._registrar(f"Saque de R$ {valor:.2f}")