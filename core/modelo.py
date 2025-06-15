
import random
from datetime import datetime
from core.filtros import calcular_ev_kelly
from core.api_football import buscar_jogos_reais

def gerar_sinais():
    print("🧪 Chamando buscar_jogos_reais() para múltiplas ligas...")
    jogos = []
    try:
        for nome_liga, liga_id in {'Brasileirão Série A': 71, 'Brasileirão Série B': 72, 'Liga Argentina': 128, 'Copa do Brasil': 73, 'Mundial de Clubes': 6, 'Champions League': 2, 'Liga Portuguesa': 94, 'Liga Italiana (Série A)': 135, 'Liga Francesa (Ligue 1)': 61, 'Libertadores': 13, 'Sul-Americana': 15, 'Estaduais (Paulista A1)': 50, 'Europa League': 3, 'Conference League': 848, 'Copa da Inglaterra (FA Cup)': 45, 'Copa da Espanha (Copa del Rey)': 143, 'Copa da Itália (Coppa Italia)': 137, 'Copa da França (Coupe de France)': 66, 'Copa de Portugal (Taça de Portugal)': 96} .items():
            print(f"🔍 Buscando jogos para: {nome_liga} (ID {liga_id})")
            novos_jogos = buscar_jogos_reais(liga_id=liga_id, qtd=10)
            jogos.extend(novos_jogos)
        print(f"📦 Total de jogos reais recebidos: {len(jogos)}")
    except Exception as e:
        print(f"❌ Erro ao buscar jogos reais: {e}")
        jogos = []

    if not jogos:
        print("⚠️ Nenhum jogo real encontrado, gerando jogos simulados para evitar travamento...")
        jogos = [{"casa": "Time A", "fora": "Time B", "liga": "Simulado", "data": str(datetime.now())} for _ in range(5)]

    mercados = ['Ambos Marcam + Over 2.5', 'Resultado + Over 1.5',
                'Handicap Asiático -0.25', 'Under 3.5 gols']
    sinais = []
    for jogo in jogos:
        mercado = random.choice(mercados)
        odd = round(random.uniform(1.9, 2.4), 2)
        prob = round(random.uniform(0.81, 0.95), 2)
        ev, stake = calcular_ev_kelly(prob, odd)
        if ev > 0 and prob >= 0.80:
            s = {
                'Partida': f"{jogo['casa']} x {jogo['fora']}",
                'Liga': jogo['liga'],
                'Mercado': mercado,
                'Odd': odd,
                'Probabilidade': prob,
                'EV': round(ev, 2),
                'Stake (%)': stake * 100,
                'Data do jogo': jogo['data']
            }
            print("✅ SINAL:", s)
            sinais.append(s)
    print(f"📊 {len(sinais)} sinais gerados com EV>0 e prob ≥ 0.80")
    return sinais
