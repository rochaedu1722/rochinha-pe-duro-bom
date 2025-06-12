
import time
from modes import modo_fusion, modo_precision, modo_laboratorio

def executar_todos_os_modos():
    print("🔁 Executando todos os modos...")
    modo_fusion.executar()
    modo_precision.executar()
    modo_laboratorio.executar()
    print("✅ Ciclo de execução finalizado.")

if __name__ == "__main__":
    while True:
        executar_todos_os_modos()
        print("⏳ Aguardando 1 hora até o próximo ciclo...")
        time.sleep(3600)  # Espera 1 hora (3600 segundos)
