from core.modelo import gerar_sinais
from core.filtros import calcular_ev_kelly
from core.telegram_sender import enviar_telegram

NOME_MODO = "modo_agressivo"

def executar():
    print("🔍 Entrando no modo_agressivo")  # <-- Adicionado
    print(f"🚀 Executando {NOME_MODO} com perfil agressivo...")
    sinais = gerar_sinais()

    sinais = gerar_sinais()

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
            enviar_telegram(mensagem)
