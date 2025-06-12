
import sqlite3
from datetime import datetime

def registrar_sinal(sinal, modo):
    try:
        conn = sqlite3.connect("db/rochinha_aprendizado_completo.db")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sinais (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT,
                jogo TEXT,
                modo TEXT,
                mercado TEXT,
                odd REAL,
                ev REAL,
                confianca INTEGER,
                resultado TEXT,
                roi REAL
            )
        """)
        cursor.execute("""
            INSERT INTO sinais (data, jogo, modo, mercado, odd, ev, confianca, resultado, roi)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            sinal.get("jogo", ""),
            modo,
            sinal.get("mercado", ""),
            sinal.get("odd", 0),
            sinal.get("ev", 0),
            sinal.get("confiança", sinal.get("confianca", 0)),
            "PENDENTE",
            0.0
        ))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Erro ao registrar sinal: {e}")
