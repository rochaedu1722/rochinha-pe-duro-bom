
print("✅ Iniciando run_scheduler.py (nível 1)")

try:
    print("🔧 Tentando importar os modos e o monitoramento...")
    from modes import modo_agressivo, modo_supremo_ml
    from core.monitoramento_padroes import verificar_padroes_de_mercado
    print("✅ Importações concluídas com sucesso.")
except Exception as e:
    print("❌ Erro ao importar módulos:")
    print(e)

import time
from datetime import datetime

ultima_varredura = None

def executar_varredura():
    global ultima_varredura
    print("🚨 Início da varredura contínua (modo 24/7)")

    while True:
        agora = datetime.now().strftime("%H:%M")
        print(f"\n⏰ Nova varredura às {agora}")

        print("🔄 [1] Iniciando varredura com modo_agressivo...")
        try:
            modo_agressivo.executar()
            print("✅ [1] Finalizou modo_agressivo.")
        except Exception as e:
            print("❌ [1] Erro no modo_agressivo:")
            print(e)

        print("🔄 [2] Iniciando varredura com modo_supremo_ml...")
        try:
            modo_supremo_ml.executar()
            print("✅ [2] Finalizou modo_supremo_ml.")
        except Exception as e:
            print("❌ [2] Erro no modo_supremo_ml:")
            print(e)

        print("🔍 [3] Iniciando verificação de padrões de mercado...")
        try:
            verificar_padroes_de_mercado()
        except Exception as e:
            print(f"❌ [3] Erro ao verificar padrões: {e}")

        print("🕒 Aguardando 10 segundos para nova varredura...\n")
        time.sleep(10)
