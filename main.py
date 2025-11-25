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