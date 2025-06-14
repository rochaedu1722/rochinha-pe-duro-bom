print("🧪 MAIN.PY: print antes de qualquer import")

try:
    print("🧪 MAIN.PY: tentando importar run_scheduler...")
    from run_scheduler import executar_varredura
    print("🧪 MAIN.PY: importação feita com sucesso!")

    if __name__ == "__main__":
        print("▶️ MAIN.PY: chamando executar_varredura...")
        executar_varredura()

except Exception as e:
    print("❌ MAIN.PY: erro detectado!")
    print(e)

print("🏁 MAIN.PY: fim.")
