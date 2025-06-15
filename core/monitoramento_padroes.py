
import sqlite3
from datetime import datetime
from core.telegram_sender import enviar_telegram

CASAS_RELEVANTES = ["bet365", "Pinnacle", "Betano"]
LIMIAR_ALERTA = 5  # mínimo de ocorrências para considerar padrão

def registrar_odd(casa, mercado, odd, probabilidade):
    ev = (probabilidade * odd) - 1
    timestamp = datetime.now().isoformat()

    conn = sqlite3.connect("db/rochinha_aprendizado_completo.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS historico_odds (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            casa TEXT,
            mercado TEXT,
            odd REAL,
            probabilidade REAL,
            ev REAL,
            timestamp TEXT
        )
    """)
    c.execute("INSERT INTO historico_odds (casa, mercado, odd, probabilidade, ev, timestamp) VALUES (?, ?, ?, ?, ?, ?)",
              (casa, mercado, odd, probabilidade, ev, timestamp))
    conn.commit()
    conn.close()

def verificar_padroes_de_mercado():
    print("📊 Verificando padrões de mercado...")
    try:
        conn = sqlite3.connect("db/rochinha_aprendizado_completo.db")
        c = conn.cursor()

        # Garante que a tabela exista
        c.execute("""
            CREATE TABLE IF NOT EXISTS historico_odds (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                casa TEXT,
                mercado TEXT,
                odd REAL,
                probabilidade REAL,
                ev REAL,
                timestamp TEXT
            )
        """)

        for casa in CASAS_RELEVANTES:
            c.execute("""
                SELECT mercado, AVG(ev) as media_ev, COUNT(*) as ocorrencias
                FROM historico_odds
                WHERE casa = ?
                GROUP BY mercado
                HAVING ocorrencias >= ? AND media_ev > 0.08
            """, (casa, LIMIAR_ALERTA))
            resultados = c.fetchall()

            for mercado, media_ev, ocorrencias in resultados:
                mensagem = (
                    f"📡 ALERTA DE PADRÃO DETECTADO\n"
                    f"🏛️ Casa: {casa}\n"
                    f"📈 Mercado: {mercado}\n"
                    f"📊 EV médio: {round(media_ev, 2)}\n"
                    f"📚 Ocorrências: {ocorrencias}\n"
                    f"💡 Possível desajuste de mercado detectado!"
                )
                enviar_telegram(mensagem)
                print("📤 Alerta de padrão enviado ao Telegram.")
    except Exception as e:
        print(f"❌ Erro ao verificar padrões de mercado: {e}")
    finally:
        conn.close()
