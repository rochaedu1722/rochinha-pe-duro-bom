
from core.telegram_sender import enviar_sinal
from core.aprendizado import registrar_sinal

def executar():
    print("🔬 [Laboratório] Testando mercados experimentais...")

    # Simulação de apostas experimentais
    sinais = [
        {"jogo": "Time E x Time F", "mercado": "Gol após 75 minutos", "odd": 2.4, "confianca": 78, "ev": 3.1},
        {"jogo": "Time G x Time H", "mercado": "Jogador X para marcar", "odd": 3.0, "confianca": 81, "ev": 2.0}
    ]

    for sinal in sinais:
        if sinal['ev'] > 0 and sinal['confianca'] >= 75:
            mensagem = f"[Lab] Mercado experimental: {sinal['jogo']} - {sinal['mercado']} @ {sinal['odd']}"
            enviar_sinal(mensagem)
            registrar_sinal(sinal, modo="laboratorio")

    print("✅ [Laboratório] Fim do experimento.")
