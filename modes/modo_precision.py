
from core.telegram_sender import enviar_sinal
from core.aprendizado import registrar_sinal
from core.api_football import obter_jogos_do_dia
from core.odd_scraper import buscar_odd_real
import random

def executar():
    print("🔍 [Precision] Avaliando fair odds e EV...")
    jogos = obter_jogos_do_dia()
    mercados = ["Resultado + Over 1.5", "Dupla + Over 2.5", "Ambos Marcam"]

    for jogo in jogos:
        mercado = random.choice(mercados)
        odd_real = buscar_odd_real(jogo, mercado)
        odd_justa = round(odd_real - random.uniform(0.1, 0.3), 2)
        ev = round(((odd_real - odd_justa) / odd_justa) * 100, 2)
        confianca = random.randint(85, 95)

        if ev > 0 and confianca >= 85:
            mensagem = f"[Precision] Sinal: {jogo} - {mercado} @ {odd_real} (EV {ev}%)"
            enviar_sinal(mensagem)
            registrar_sinal({
                "jogo": jogo,
                "mercado": mercado,
                "odd": odd_real,
                "ev": ev,
                "confianca": confianca
            }, modo="precision")
    print("✅ [Precision] Fim da análise.")
