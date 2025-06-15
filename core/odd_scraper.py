
import random

USE_REAL_API = False  # Troque para True se quiser usar TheOddsAPI real

def buscar_odd_real(jogo, mercado):
    if USE_REAL_API:
        # Aqui entraria chamada real à TheOddsAPI com sua chave
        raise NotImplementedError("Integração com TheOddsAPI ainda não implementada.")
    else:
        # Simulação de odd com base no mercado
        base = {
            "Mais de 2.5 gols": 2.0,
            "Ambos Marcam": 1.9,
            "Resultado + Over 1.5": 2.2,
            "Dupla + Over 2.5": 2.5,
            "Gol após 75 minutos": 2.8,
            "Jogador para marcar": 3.0,
            "Finalizações por tempo": 2.6
        }
        odd = base.get(mercado, 2.0)
        variacao = random.uniform(-0.2, 0.3)
        return round(odd + variacao, 2)
