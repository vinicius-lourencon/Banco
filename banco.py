from typing import Dict

from cliente import Cliente
from conta import Conta
from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca
from excecoes import ContaNaoEncontradaError, ErroBanco

class Banco:
    """
    Representa um banco simples responsável por gerenciar clientes e contas.

    Esta classe oferece métodos para cadastrar clientes, abrir contas e realizar
    operações como depósito, saque, transferência e emissão de extrato.
    """

    def __init__(self, nome: str) -> None:
        """
        Inicializa uma nova instância de Banco.

        :nome: Nome do banco.
        """
        self._nome: str = nome
        self._clientes: Dict[str, Cliente] = {}  # chave: CPF
        self._contas: Dict[str, Conta] = {}      # chave: número da conta

