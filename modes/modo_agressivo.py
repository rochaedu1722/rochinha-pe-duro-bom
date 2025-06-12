
from core.modelo import gerar_sinais
from core.utils import calcular_kelly, enviar_telegram
from db.database import registrar_aposta
import time

NOME_MODO = "modo_agressivo"

MERCADOS = [
    "handicap_asiatico_menos_025",
    "ambos_marcam",
    "resultado",
    "over_25",
    "dupla_chance_over_15"
]

def executar():
    print(f"🚀 Executando {NOME_MODO} com perfil agressivo...")

    sinais = gerar_sinais(
        mercados=MERCADOS,
        prob_minima=0.80,
        somente_valor_esperado_positivo=True
    )

    for sinal in sinais:
        odd = sinal['odd']
        prob = sinal['probabilidade']
        ev = (odd * prob) - 1
        stake = calcular_kelly(odd, prob)

        if stake > 0:
            mensagem = (
                f"🔥 SINAL [{NOME_MODO.upper()}]\n"
                f"🧠 Mercado: {sinal['mercado']}\n"
                f"🏟️ Jogo: {sinal['jogo']}\n"
                f"📊 Prob: {round(prob * 100, 2)}%\n"
                f"💰 Odd: {odd}\n"
                f"✅ EV: {round(ev, 2)}\n"
                f"🎯 Stake: {round(stake, 2)}u"
            )

            enviar_telegram(mensagem)
            registrar_aposta(sinal, stake, NOME_MODO)

    time.sleep(2)
