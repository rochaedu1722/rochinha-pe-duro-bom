print("🧪 MAIN.PY: início da execução")

try:
    print("🧪 MAIN.PY: tentando importar run_scheduler...")
    from run_scheduler import executar_varredura
    print("✅ MAIN.PY: importação concluída com sucesso.")

    if __name__ == "__main__":
        print("▶️ MAIN.PY: chamando executar_varredura()...")
        executar_varredura()

except Exception as e:
    print("❌ MAIN.PY: erro durante execução")
    print(e)
    print("🏁 MAIN.PY: finalizado por erro")
