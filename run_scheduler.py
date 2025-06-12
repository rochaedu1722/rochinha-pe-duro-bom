import time
from modes import modo_supremo_ml  # Importação corrigida

def loop_execucao():
    while True:
        print("🔁 Executando varredura do modo_supremo_ml...")
        try:
            modo_supremo_ml.executar()
        except Exception as e:
            print(f"⚠️ Erro durante execução: {e}")
        print("⏱️ Aguardando 1 hora para próxima varredura...\n")
        time.sleep(3600)  # Espera 3600 segundos (1 hora)

if __name__ == "__main__":
    loop_execucao()
