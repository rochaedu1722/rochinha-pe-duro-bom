print("✅ Iniciando run_scheduler.py (nível 1)")

try:
    from modes import modo_agressivo, modo_supremo_ml
    print("✅ Importação dos modos concluída.")
except Exception as e:
    print("❌ Erro ao importar modos:")
    print(e)

import time

def executar_varredura():
    print("🚨 Início da varredura contínua (modo 24/7)")

    while True:
        print("🔄 Varrendo sinais com modo_agressivo...")
        try:
            modo_agressivo.executar()
        except Exception as e:
            print(f"❌ Erro no modo_agressivo: {e}")

        print("🔄 Varrendo sinais com modo_supremo_ml...")
        try:
            modo_supremo_ml.executar()
        except Exception as e:
            print(f"❌ Erro no modo_supremo_ml: {e}")

        print("🕒 Aguardando 900 segundos para nova varredura...")
        time.sleep(900)  # ⏱️ Tempo reduzido só para testes
