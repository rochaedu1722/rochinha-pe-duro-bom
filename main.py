print("✅ MAIN.PY: Iniciando debug...")

try:
    print("🧪 Tentando importar run_scheduler...")
    import run_scheduler
    print("✅ Importação de run_scheduler OK.")
except Exception as e:
    print("❌ ERRO ao importar run_scheduler:")
    print(e)

print("🏁 Fim do main.py.")
