# Funções auxiliares e cálculo de fair odds

def calcular_kelly(probabilidade: float, odd: float, fracao: float = 1.0) -> float:
    """
    Calcula a fração de stake com base no critério de Kelly.
    """
    valor = (probabilidade * (odd - 1) - (1 - probabilidade)) / (odd - 1)
    valor_kelly = max(valor, 0)
    return round(valor_kelly * fracao, 4)