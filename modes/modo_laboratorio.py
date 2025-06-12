
from core.telegram_sender import enviar_sinal
from core.aprendizado import registrar_sinal
from core.api_football import obter_jogos_do_dia
from core.odd_scraper import buscar_odd_real
import random

def executar():
    print("🔬 [Laboratório] Testando sinais ousados...")
    jogos = obter_jogos_do_dia()
    mercados = ["Gol após 75 minutos", "Jogador para marcar", "Finalizações por tempo"]

    for jogo in jogos:
        mercado = random.choice(mercados)
        odd = buscar_odd_real(jogo, mercado)
        ev = round(random.uniform(1.5, 6.0), 2)
        confianca = random.randint(75, 90)

        if ev > 0 and confianca >= 75:
            mensagem = f"[Lab] Experimento: {jogo} - {mercado} @ {odd} (EV {ev}%)"
            enviar_sinal(mensagem)
            registrar_sinal({
                "jogo": jogo,
                "mercado": mercado,
                "odd": odd,
                "ev": ev,
                "confianca": confianca
            }, modo="laboratorio")
    print("✅ [Laboratório] Fim do experimento.")
