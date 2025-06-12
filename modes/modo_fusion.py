
# modo_fusion.py

from core.odds_checker import obter_odds_reais_simuladas, verificar_value_bet
import sqlite3

def calcular_odd_justa_por_confianca(confianca):
    probabilidade = confianca / 100
    return round(1 / probabilidade, 2)

def consultar_padrao_vencedor(liga, mercado):
    conn = sqlite3.connect("db/rochinha_aprendizado_completo.db")
    query = """
        SELECT roi FROM aprendizado_resultado
        WHERE liga = ? AND mercado = ?
        ORDER BY data_ultima_atualizacao DESC LIMIT 1
    """
    cursor = conn.cursor()
    cursor.execute(query, (liga, mercado))
    resultado = cursor.fetchone()
    conn.close()
    return resultado and resultado[0] > 0

def executar():
    print("🚀 Executando MODO FUSION... IA cruzada, odds e padrão ROI")

    partidas_simuladas = [
        {"liga": "Premier League", "jogo": "Liverpool x Arsenal", "mercado": "Mais de 2.5 gols", "confianca": 91},
        {"liga": "La Liga", "jogo": "Real Madrid x Girona", "mercado": "BTTS", "confianca": 89},
        {"liga": "Brasileirão", "jogo": "Flamengo x Botafogo", "mercado": "Resultado + Over 1.5", "confianca": 93}
    ]

    for partida in partidas_simuladas:
        odd_justa = calcular_odd_justa_por_confianca(partida["confianca"])
        odds_reais = obter_odds_reais_simuladas(partida["jogo"])
        oportunidades = verificar_value_bet(odd_justa, odds_reais)

        padrao_ok = consultar_padrao_vencedor(partida["liga"], partida["mercado"])

        if oportunidades and padrao_ok:
            melhor_op = max(oportunidades, key=lambda x: x["ev_percentual"])
            print(f"""
[FUSION] 💡 Sinal detectado:
🏆 Liga: {partida['liga']}
📌 Jogo: {partida['jogo']}
🎯 Mercado: {partida['mercado']}
🔒 Confiança: {partida['confianca']}%
📊 Odd Justa: {odd_justa}
💰 Odd Real (Value): {melhor_op['odd']} na {melhor_op['casa']}
🧠 EV: {melhor_op['ev_percentual']}%
✅ Padrão de ROI confirmado
            """)
        else:
            print(f"⛔ {partida['jogo']} ignorado no Fusion: Sem value bet ou ROI negativo.")
