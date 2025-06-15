
import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_FOOTBALL_KEY")

LIGAS_MONITORADAS = {
    "Premier League": 39,
    "La Liga": 140,
    "Serie A": 135,
    "Bundesliga": 78,
    "Ligue 1": 61,
    "Brasileirão Série A": 71,
    "Libertadores": 13,
    "Champions League": 2,
    "Liga Portugal": 94,
    "Campeonato Argentino": 128,
    "Copa do Mundo de Clubes FIFA": 6
}

def buscar_jogos_reais(qtd_por_liga=5, temporada=2025):
    headers = {"x-apisports-key": API_KEY}
    todos_os_jogos = []

    for nome_liga, liga_id in LIGAS_MONITORADAS.items():
        url = f"https://v3.football.api-sports.io/fixtures?league={liga_id}&season={temporada}&next={qtd_por_liga}"
        try:
            resposta = requests.get(url, headers=headers, timeout=10)
            if resposta.status_code == 200:
                jogos = resposta.json().get("response", [])
                for j in jogos:
                    todos_os_jogos.append({
                        "data": j["fixture"]["date"],
                        "casa": j["teams"]["home"]["name"],
                        "fora": j["teams"]["away"]["name"],
                        "liga": j["league"]["name"]
                    })
            else:
                print(f"⚠️ API {nome_liga} retornou status {resposta.status_code}")
        except Exception as e:
            print(f"❌ Erro ao buscar jogos da liga {nome_liga}: {e}")

    return todos_os_jogos
