print("✅ Iniciando main.py")

try:
    from run_scheduler import executar_varredura
    print("🧪 Importação do run_scheduler concluída.")

    if __name__ == "__main__":
        print("▶️ Chamando executar_varredura()...")
        executar_varredura()

except Exception as e:
    print("❌ Erro durante execução do main.py:")
    print(e)
