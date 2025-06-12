
import requests
from datetime import datetime
import json

USE_REAL_API = True

# Carregar a chave da API do config.json
with open("config.json", "r") as f:
    config = json.load(f)

API_KEY = config.get("api_football_key")

def obter_jogos_do_dia():
    if USE_REAL_API and API_KEY:
        hoje = datetime.today().strftime("%Y-%m-%d")
        url = f"https://v3.football.api-sports.io/fixtures?date={hoje}"
        headers = {
            "x-apisports-key": API_KEY
        }

        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Erro na API: {response.status_code}")
            return []

        data = response.json()
        jogos = []
        for fixture in data["response"]:
            home = fixture["teams"]["home"]["name"]
            away = fixture["teams"]["away"]["name"]
            jogos.append(f"{home} x {away}")
        return jogos
    else:
        print("🔒 API real desativada ou chave ausente. Nenhum jogo carregado.")
        return []
