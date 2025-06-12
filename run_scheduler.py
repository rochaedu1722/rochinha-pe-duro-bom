import time
from modes import modo_supremo_ml

while True:
    print("🔁 Verificando novos jogos...")
    modo_supremo_ml.executar()
    time.sleep(3600)  # espera 1 hora antes da próxima análise
