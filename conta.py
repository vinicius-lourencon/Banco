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