
# core/odds_checker.py
import requests

API_KEY = "716f8d3daaf79e64a6efe3e0a5b76987"
BASE_URL = "https://v3.football.api-sports.io/odds"

HEADERS = {
    "x-apisports-key": API_KEY
}

def obter_odds_reais_api(league_id, fixture_id, market="over_2_5"):
    url = f"{BASE_URL}?fixture={fixture_id}&bookmaker=6"  # 6 = Bet365 (exemplo)
    try:
        response = requests.get(url, headers=HEADERS)
        data = response.json()
        odds = {}

        for item in data.get("response", []):
            for value in item.get("bookmakers", []):
                casa = value.get("name", "")
                for bet in value.get("bets", []):
                    if market in bet.get("name", "").lower():
                        for linha in bet.get("values", []):
                            label = linha.get("value", "over")
                            odd = linha.get("odd", None)
                            odds[f"{casa} - {label}"] = float(odd)
        return odds
    except Exception as e:
        print("Erro ao obter odds da API-Sports:", e)
        return {}

def verificar_value_bet(odd_justa, odds_reais, margem_minima=0.05):
    oportunidades = []
    for casa, odd in odds_reais.items():
        try:
            ev = (odd - odd_justa) / odd_justa
            if ev >= margem_minima:
                oportunidades.append({
                    "casa": casa,
                    "odd": odd,
                    "ev_percentual": round(ev * 100, 2),
                    "value_bet": True
                })
        except:
            continue
    return oportunidades
