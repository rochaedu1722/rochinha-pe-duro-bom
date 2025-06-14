import random
from datetime import datetime
from core.filtros import calcular_ev_kelly
from core.api_football import buscar_jogos_reais

def gerar_sinais():
    print("🧪 Chamando buscar_jogos_reais()...")
    try:
        jogos = buscar_jogos_reais()
    except Exception as e:
        print(f"❌ Erro ao buscar jogos reais: {e}")
        jogos = []  # fallback para evitar travamento

    mercados = ['Ambos Marcam + Over 2.5', 'Resultado + Over 1.5',
                'Handicap Asiático -0.25', 'Under 3.5 gols']
    sinais = []
    for jogo in jogos:
        mercado = random.choice(mercados)
        odd = round(random.uniform(1.9, 2.4), 2)
        prob = round(random.uniform(0.81, 0.95), 2)
        ev, stake = calcular_ev_kelly(prob, odd)
        if ev > 0 and prob >= 0.80:
            sinais.append({
                'Partida': f"{jogo['casa']} x {jogo['fora']}",
                'Liga': jogo['liga'],
                'Mercado': mercado,
                'Odd': odd,
                'Probabilidade': prob,
                'EV': round(ev, 2),
                'Stake (%)': stake * 100,
                'Data do jogo': jogo['data']
            })
    return sinais
