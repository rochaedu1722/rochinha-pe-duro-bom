from core.modelo import gerar_sinais
from core.telegram_sender import enviar_telegram_sinal
from core.aprendizado import registrar_sinal

NOME_MODO = "modo_supremo_ml"

def executar():
    print(f"🚀 Executando {NOME_MODO} com IA preditiva calibrada...")

    sinais = gerar_sinais()

    if not sinais:
        print("⚠️ Nenhum sinal gerado nesta varredura.")
    else:
        print(f"✅ {len(sinais)} sinal(is) gerado(s). Avaliando e enviando...")

    for sinal in sinais:
        prob = sinal.get("Probabilidade", 0)
        odd = sinal.get("Odd")
        mercado = sinal.get("Mercado")
        partida = sinal.get("Partida")

        mensagem = (
            f"🤖 SINAL [{NOME_MODO.upper()}]\n"
            f"🧠 Mercado: {mercado}\n"
            f"🏟️ Jogo: {partida}\n"
            f"📊 Prob: {round(prob * 100, 2)}%\n"
            f"💰 Odd: {odd}\n"
        )

        sinal_dict = {
            "jogo": partida,
            "mercado": mercado,
            "odd": odd,
            "ev": (prob * odd) - 1,  # EV estimado
            "confiança": round(prob * 100, 2)
        }

        enviar_telegram_sinal(sinal_dict, NOME_MODO, mensagem)
        registrar_sinal(sinal_dict, NOME_MODO)
        print("📤 Sinal registrado e enviado com sucesso.")
