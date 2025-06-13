from core.modelo import gerar_sinais
from core.telegram_sender import enviar_telegram

NOME_MODO = "modo_supremo_ml"

def executar():
    print(f"🚀 Executando {NOME_MODO} com IA preditiva calibrada...")

    sinais = gerar_sinais()

    if not sinais:
        print("⚠️ Nenhum sinal gerado nesta varredura.")
    else:
        print(f"✅ {len(sinais)} sinal(is) gerado(s). Enviando ao Telegram...")

    for sinal in sinais:
        mensagem = (
            f"🤖 SINAL [{NOME_MODO.upper()}]\n"
            f"🧠 Mercado: {sinal.get('Mercado')}\n"
            f"🏟️ Jogo: {sinal.get('Partida')}\n"
            f"📊 Prob: {round(sinal.get('Probabilidade', 0) * 100, 2)}%\n"
            f"💰 Odd: {sinal.get('Odd')}\n"
        )
        enviar_telegram(mensagem)
        print("📤 Sinal enviado com sucesso.")
