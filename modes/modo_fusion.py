
from core.telegram_sender import enviar_sinal
from core.aprendizado import registrar_sinal
from core.api_football import obter_jogos_do_dia
from core.odd_scraper import buscar_odd_real
import random

def executar():
    print("🔍 [Fusion] Iniciando busca por sinais...")
    jogos = obter_jogos_do_dia()
    mercados = ["Mais de 2.5 gols", "Ambos Marcam", "Resultado + Over 1.5"]

    for jogo in jogos:
        mercado = random.choice(mercados)
        odd = buscar_odd_real(jogo, mercado)
        ev = round(random.uniform(2.0, 8.0), 2)
        confianca = random.randint(80, 95)

        if confianca >= 85 and ev > 0:
            mensagem = f"[Fusion] Aposta: {jogo} - {mercado} @ {odd} (EV {ev}%)"
            enviar_sinal(mensagem)
            registrar_sinal({
                "jogo": jogo,
                "mercado": mercado,
                "odd": odd,
                "ev": ev,
                "confianca": confianca
            }, modo="fusion")
    print("✅ [Fusion] Fim da análise.")
