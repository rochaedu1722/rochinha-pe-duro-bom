
from core.telegram_sender import enviar_sinal
from core.aprendizado import registrar_sinal

def executar():
    print("🔍 [Precision] Analisando valor esperado e fair odds...")

    # Simulação de sinal com EV positivo
    sinais = [
        {"jogo": "Time C x Time D", "mercado": "Resultado + Over 1.5", "odd": 2.1, "odd_justa": 1.85, "ev": 6.5, "confianca": 90}
    ]

    for sinal in sinais:
        if sinal['ev'] > 0 and sinal['confianca'] >= 85:
            mensagem = f"[Precision] Sinal com valor: {sinal['jogo']} - {sinal['mercado']} @ {sinal['odd']} (EV {sinal['ev']}%)"
            enviar_sinal(mensagem)
            registrar_sinal(sinal, modo="precision")

    print("✅ [Precision] Fim da análise.")
