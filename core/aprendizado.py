
import sqlite3
from datetime import datetime, timedelta

db_path = "db/rochinha_aprendizado_completo.db"

def registrar_sinal(sinal, modo):
    try:
        conn = sqlite3.connect(db_path)
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
            sinal.get("confianÃ§a", sinal.get("confianca", 0)),
            "PENDENTE",
            0.0
        ))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Erro ao registrar sinal: {e}")

def sinal_ja_enviado(jogo, mercado, odd, minutos=15):
    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS sinais_enviados (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                jogo TEXT,
                mercado TEXT,
                odd REAL,
                timestamp TEXT
            )
        """)
        limite_tempo = datetime.now() - timedelta(minutes=minutos)
        c.execute("""
            SELECT 1 FROM sinais_enviados 
            WHERE jogo = ? AND mercado = ? AND odd = ? AND timestamp > ?
        """, (jogo, mercado, odd, limite_tempo.isoformat()))
        existe = c.fetchone() is not None
        conn.close()
        return existe
    except Exception as e:
        print(f"Erro ao verificar sinal duplicado: {e}")
        return False

def registrar_sinal_enviado(jogo, mercado, odd):
    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        timestamp = datetime.now().isoformat()
        c.execute("""
            INSERT INTO sinais_enviados (jogo, mercado, odd, timestamp)
            VALUES (?, ?, ?, ?)
        """, (jogo, mercado, odd, timestamp))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Erro ao registrar sinal enviado: {e}")
