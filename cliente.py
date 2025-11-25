class Cliente:
    """
    Representa um cliente do banco.

    Armazena informações básicas de identificação como nome, CPF e telefone.
    """

    def __init__(self, nome: str, cpf: str, telefone: str) -> None:
        """
        Inicializa um novo cliente.

        :nome: Nome completo do cliente.
        :cpf: CPF do cliente (apenas formato string, sem validação).
        :telefone: Telefone de contato do cliente.
        """
        self._nome: str = nome
        self._cpf: str = cpf
        self._telefone: str = telefone