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
    
 # ---------- CONTAS ----------

    def abrir_conta_corrente(
        self,
        numero: str,
        cpf_cliente: str,
        saldo_inicial: float = 0.0,
        limite: float = 0.0,
    ) -> ContaCorrente:
        """
        Abre uma nova conta corrente para um cliente existente.

        :numero: Número da conta.
        :cpf_cliente: CPF do cliente já cadastrado.
        :saldo_inicial: Saldo inicial da conta.
        :limite: Limite da conta corrente.
        :return: Instância de ContaCorrente criada.
        :raises ErroBanco: Se o cliente não for encontrado.
        """
        cliente: Cliente = self._obter_cliente_por_cpf(cpf_cliente)
        conta = ContaCorrente(numero, cliente, saldo_inicial, limite)
        self._contas[numero] = conta
        return conta