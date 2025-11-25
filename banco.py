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

# ---------- CLIENTE ----------

    def cadastrar_cliente(self, nome: str, cpf: str, telefone: str) -> Cliente:
        """
        Cadastra ou atualiza um cliente no banco.

        Se o CPF já existir, o cadastro é sobrescrito (sem exceção, apenas aviso).

        :nome: Nome do cliente.
        :cpf: CPF do cliente.
        :telefone: Telefone do cliente.
        :return: Instância de Cliente criada ou atualizada.
        """
        if cpf in self._clientes:
            print("Aviso: CPF já existia, dados do cliente foram atualizados.")
        cliente = Cliente(nome, cpf, telefone)
        self._clientes[cpf] = cliente
        return cliente
