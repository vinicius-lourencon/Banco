from banco import Banco


def ler_float(mensagem: str) -> float:
    """
    Lê um valor numérico de ponto flutuante digitado pelo usuário.

    A função continua perguntando até que um valor válido seja informado.
    Também aceita vírgula como separador decimal.

    :param mensagem: Texto a ser exibido para o usuário.
    :return: Valor convertido para float.
    """
    while True:
        try:
            texto: str = input(mensagem).strip().replace(",", ".")
            valor: float = float(texto)
            return valor
        except ValueError:
            print("Valor numérico inválido, tente novamente.")
    
def menu() -> None:
    """
    Exibe o menu principal do sistema bancário e controla o fluxo da aplicação.

    Esta função é o ponto de entrada da interface em modo texto.
    """
    banco = Banco("Banco do Vinícius")

    while True:
        print("\n=== MENU DO BANCO ===")
        print("1 - Cadastrar cliente")
        print("2 - Abrir conta corrente")
        print("3 - Abrir conta poupança")
        print("4 - Depositar")
        print("5 - Sacar")
        print("6 - Transferir")
        print("7 - Extrato")
        print("8 - Listar contas")
        print("0 - Sair")

        opcao: str = input("Escolha uma opção: ").strip()

        if opcao == "0":
            print("Saindo... Obrigado por usar o Banco do Vinícius!")
            break

        try:
            if opcao == "1":
                nome: str = input("Nome do cliente: ")
                cpf: str = input("CPF: ")
                telefone: str = input("Telefone: ")
                banco.cadastrar_cliente(nome, cpf, telefone)
                print("Cliente cadastrado com sucesso.")

            elif opcao == "2":
                numero: str = input("Número da conta: ")
                cpf: str = input("CPF do cliente: ")
                saldo_inicial: float = ler_float("Saldo inicial: R$ ")
                limite: float = ler_float("Limite da conta corrente: R$ ")
                banco.abrir_conta_corrente(numero, cpf, saldo_inicial, limite)
                print("Conta corrente aberto com sucesso.")

            elif opcao == "3":
                numero: str = input("Número da conta: ")
                cpf: str = input("CPF do cliente: ")
                saldo_inicial: float = ler_float("Saldo inicial: R$ ")
                banco.abrir_conta_poupanca(numero, cpf, saldo_inicial)
                print("Conta poupança aberta com sucesso.")
