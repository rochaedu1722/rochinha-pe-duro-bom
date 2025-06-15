from core.modelo import gerar_sinais
from core.filtros import calcular_ev_kelly
from core.telegram_sender import enviar_telegram_sinal
from core.aprendizado import registrar_sinal

NOME_MODO = "modo_agressivo"

def executar():
    print("🔍 Entrando no modo_agressivo")
    print(f"🚀 Executando {NOME_MODO} com perfil agressivo...")

    sinais = gerar_sinais()

    # Envio de sinal de teste
    from core.telegram_sender import enviar_telegram_sinal
    enviar_telegram_sinal(
        {"jogo": "Teste FC x Bot Agressivo", "mercado": "Resultado + Over 1.5", "odd": 2.3, "ev": 0.18, "confiança": 85.0},
        NOME_MODO,
        "🧪 Sinal de teste do modo agressivo enviado para verificar o Telegram."
    )

    if not sinais:
        print("⚠️ Nenhum sinal gerado nesta varredura.")
    else:
        print(f"✅ {len(sinais)} sinal(is) encontrado(s). Avaliando EV...")

    for sinal in sinais:
        odd = sinal['Odd']
        prob = sinal['Probabilidade']
        ev, stake = calcular_ev_kelly(prob, odd)

        if ev > 0:
            mensagem = (
                f"🔥 SINAL [{NOME_MODO.upper()}]\n"
                f"🧠 Mercado: {sinal['Mercado']}\n"
                f"🏟️ Jogo: {sinal['Partida']}\n"
                f"📊 Prob: {round(prob * 100, 2)}%\n"
                f"💰 Odd: {odd}\n"
                f"✅ EV: {round(ev, 2)}\n"
                f"📈 Stake sugerida: {round(stake * 100, 2)}%"
            )

            # Adaptar dicionário para o formato aceito pela IA e banco
            sinal_dict = {
                "jogo": sinal["Partida"],
                "mercado": sinal["Mercado"],
                "odd": odd,
                "ev": ev,
                "confiança": round(prob * 100, 2)
            }

            enviar_telegram_sinal(sinal_dict, NOME_MODO, mensagem)
            registrar_sinal(sinal_dict, NOME_MODO)
            print("📤 Sinal registrado e enviado com sucesso.")
