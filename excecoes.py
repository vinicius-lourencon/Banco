class ErroBanco(Exception):
    """Exceção base para o sistema do banco."""
    pass

class ContaNaoEncontradaError(ErroBanco):
    def __init__(self, numero_conta: str):
        super().__init__(f"Conta '{numero_conta}' não encontrada.")