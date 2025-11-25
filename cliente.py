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


    @property
    def nome(self) -> str:
        """
        Retorna o nome do cliente.
        """
        return self._nome

    @property
    def cpf(self) -> str:
        """
        Retorna o CPF do cliente.

        """
        return self._cpf

    @property
    def telefone(self) -> str:
        """
        Retorna o telefone do cliente.
        """
        return self._telefone

    def __str__(self) -> str:
        """
        Retorna a representação em texto do cliente.

        :return: String formatada com nome e CPF do cliente.
        """
        return f"{self._nome} (CPF: {self._cpf})"