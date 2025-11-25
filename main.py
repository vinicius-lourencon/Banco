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