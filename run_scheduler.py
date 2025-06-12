
import time
from modes import modo_agressivo, modo_supremo_ml

if __name__ == "__main__":
    while True:
        print("🔄 Varrendo sinais com modo_agressivo...")
        modo_agressivo.executar()

        print("🔄 Varrendo sinais com modo_supremo_ml...")
        modo_supremo_ml.executar()

        print("🕒 Aguardando 1 hora para nova varredura...")
        time.sleep(3600)
