from core.modelo import gerar_sinais
from core.telegram_sender import enviar_telegram

def executar():
    sinais = gerar_sinais()
    for sinal in sinais:
        mensagem = f"📢 NOVO SINAL\n{str(sinal)}"
        enviar_telegram(mensagem)