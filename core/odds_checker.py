
# odds_checker.py

import random

def obter_odds_reais_simuladas(jogo):
    # Simulação de consulta às odds reais de casas como Betano, Bet365
    return {
        "Betano": round(random.uniform(1.60, 2.10), 2),
        "Bet365": round(random.uniform(1.55, 2.20), 2),
        "Pinnacle": round(random.uniform(1.65, 2.05), 2)
    }

def verificar_value_bet(odd_justa, odds_reais, margem_minima=0.05):
    oportunidades = []
    for casa, odd in odds_reais.items():
        ev = (odd - odd_justa) / odd_justa
        if ev >= margem_minima:
            oportunidades.append({
                "casa": casa,
                "odd": odd,
                "ev_percentual": round(ev * 100, 2),
                "value_bet": True
            })
    return oportunidades
