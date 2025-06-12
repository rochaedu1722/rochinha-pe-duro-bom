
# run_scheduler.py

import schedule
import time
import datetime
from modes import modo_fusion, precision_v4, laboratorio_v2
from core.telegram_sender import enviar_mensagem

def executar_todos_os_modos():
    horario = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    enviar_mensagem(f"🟢 Executando bot Rochinha às {horario}")
    print(f"🟢 Executando bot Rochinha às {horario}")

    try:
        precision_v4.executar()
        laboratorio_v2.executar()
        modo_fusion.executar()
    except Exception as e:
        print("Erro ao executar modos:", e)
        enviar_mensagem(f"⚠️ Erro ao executar modos: {e}")

# Executa os modos a cada 30 minutos
schedule.every(30).minutes.do(executar_todos_os_modos)

print("⏱️ Agendador do Bot Rochinha iniciado...")

# Executa em loop contínuo
while True:
    schedule.run_pending()
    time.sleep(1)
