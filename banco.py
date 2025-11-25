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
    

    def abrir_conta_poupanca(
        self,
        numero: str,
        cpf_cliente: str,
        saldo_inicial: float = 0.0,
    ) -> ContaPoupanca:
        """
        Abre uma nova conta poupança para um cliente existente.

        :numero: Número da conta.
        :cpf_cliente: CPF do cliente já cadastrado.
        :saldo_inicial: Saldo inicial da conta.
        :return: Instância de ContaPoupanca criada.
        :raises ErroBanco: Se o cliente não for encontrado.
        """
        cliente: Cliente = self._obter_cliente_por_cpf(cpf_cliente)
        conta = ContaPoupanca(numero, cliente, saldo_inicial)
        self._contas[numero] = conta
        return conta


    def _obter_cliente_por_cpf(self, cpf: str) -> Cliente:
        """
        Busca um cliente pelo CPF.

        :cpf: CPF do cliente.
        :return: Instância de Cliente encontrada.
        :raises ErroBanco: Se o cliente não for encontrado.
        """
        cliente = self._clientes.get(cpf)
        if not cliente:
            raise ErroBanco(f"Cliente com CPF {cpf} não encontrado.")
        return cliente

    def _obter_conta(self, numero: str) -> Conta:
        """
        Busca uma conta pelo número.

        :numero: Número da conta.
        :return: Instância de Conta encontrada.
        :raises ContaNaoEncontradaError: Se a conta não for localizada.
        """
        conta = self._contas.get(numero)
        if not conta:
            raise ContaNaoEncontradaError(numero)
        return conta
    
    # ---------- OPERAÇÕES -----------------
    
    def depositar(self, numero_conta: str, valor: float) -> None:
        """
        Realiza um depósito em uma conta específica.

        Esta função trata internamente as exceções e exibe mensagens
        de erro amigáveis para o usuário.

        :numero_conta: Número da conta que receberá o depósito.
        :valor: Valor a ser depositado.
        """
        try:
            conta: Conta = self._obter_conta(numero_conta)
            conta.depositar(valor)
            print(f"Depósito realizado com sucesso. Novo saldo: R$ {conta.saldo:.2f}")
        except (ErroBanco, ValueError, TypeError) as e:
            print(f"[ERRO AO DEPOSITAR] {e}")

    def sacar(self, numero_conta: str, valor: float) -> None:
        """
        Realiza um saque em uma conta específica.

        O método captura exceções específicas de negócio (como saldo insuficiente)
        e também erros de tipo/valor.

        :numero_conta: Número da conta de onde será feito o saque.
        :valor: Valor a ser sacado.
        """
        try:
            conta: Conta = self._obter_conta(numero_conta)
            conta.sacar(valor)
            print(f"Saque realizado com sucesso. Novo saldo: R$ {conta.saldo:.2f}")
        except (ErroBanco, ValueError, TypeError) as e:
            print(f"[ERRO AO SACAR] {e}")


    def transferir(self, numero_origem: str, numero_destino: str, valor: float) -> None:
        """
        Realiza uma transferência entre duas contas.

        :umero_origem: Número da conta de origem.
        :numero_destino: Número da conta de destino.
        :valor: Valor a ser transferido.
        """
        try:
            conta_origem: Conta = self._obter_conta(numero_origem)
            conta_destino: Conta = self._obter_conta(numero_destino)

            conta_origem.sacar(valor)
            conta_destino.depositar(valor)
            print("Transferência realizada com sucesso.")
        except (ErroBanco, ValueError, TypeError) as e:
            print(f"[ERRO NA TRANSFERÊNCIA] {e}")

    def mostrar_extrato(self, numero_conta: str) -> None:
        """
        Exibe o extrato de uma conta no terminal.

        :numero_conta: Número da conta cujo extrato será exibido.
        """
        try:
            conta: Conta = self._obter_conta(numero_conta)
            print(conta.extrato())
        except ErroBanco as e:
            print(f"[ERRO AO GERAR EXTRATO] {e}")

    def listar_contas(self) -> None:
        """
        Lista todas as contas cadastradas no banco.

        As informações são exibidas diretamente no terminal.
        """
        if not self._contas:
            print("Nenhuma conta cadastrada.")
            return
        for conta in self._contas.values():
            print(conta)