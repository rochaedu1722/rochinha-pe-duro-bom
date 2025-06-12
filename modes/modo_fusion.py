
from core.telegram_sender import enviar_sinal
from core.aprendizado import registrar_sinal

def executar():
    print("🔍 [Fusion] Iniciando busca por sinais...")

    # Simulação de lógica intermediária entre segurança e volume
    sinais = [
        {"jogo": "Time A x Time B", "mercado": "Mais de 2.5 gols", "odd": 1.95, "confianca": 87, "ev": 4.5}
    ]

    for sinal in sinais:
        if sinal['confianca'] >= 85 and sinal['ev'] > 0:
            mensagem = f"[Fusion] Aposta encontrada: {sinal['jogo']} - {sinal['mercado']} @ {sinal['odd']}"
            enviar_sinal(mensagem)
            registrar_sinal(sinal, modo="fusion")

    print("✅ [Fusion] Fim da análise.")
