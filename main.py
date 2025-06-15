import sys
import traceback

print("✅ MAIN.PY: entrou no arquivo")

try:
    print("🟢 MAIN.PY: tentando importar run_scheduler...")
    from run_scheduler import executar_varredura
    print("🟢 MAIN.PY: importação bem-sucedida")

    if __name__ == "__main__":
        print("🟢 MAIN.PY: __name__ é '__main__' ✅")
        executar_varredura()

except Exception as e:
    print("❌ MAIN.PY: erro detectado")
    traceback.print_exc()  # Exibe erro completo com stack trace
    sys.stdout.flush()
    sys.stderr.flush()
    print("🏁 MAIN.PY: finalizado por erro")
