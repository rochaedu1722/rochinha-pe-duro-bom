import requests

API_KEY = "716f8d3daaf79e64a6efe3e0a5b76987"

def buscar_jogos_reais(liga_id=39, qtd=10):
    url = f"https://v3.football.api-sports.io/fixtures?league={liga_id}&season=2025&next={qtd}"
    headers = {"x-apisports-key": API_KEY}
    try:
        resposta = requests.get(url, headers=headers, timeout=10)
        if resposta.status_code == 200:
            jogos = resposta.json().get("response", [])
            return [{
                "data": j["fixture"]["date"],
                "casa": j["teams"]["home"]["name"],
                "fora": j["teams"]["away"]["name"],
                "liga": j["league"]["name"]
            } for j in jogos]
        else:
            print(f"⚠️ API retornou status {resposta.status_code}")
    except Exception as e:
        print(f"❌ Erro ao acessar API: {e}")
    return []
