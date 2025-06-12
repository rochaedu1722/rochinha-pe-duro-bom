
# aprendizado_continuo.py

import sqlite3
import pandas as pd
from datetime import datetime

def executar_aprendizado(banco_path="db/rochinha_aprendizado_completo.db"):
    conn = sqlite3.connect(banco_path)
    df = pd.read_sql_query("SELECT * FROM apostas", conn)

    if df.empty:
        print("Nenhuma aposta registrada ainda.")
        return

    resumo = (
        df.groupby(["modo_gerador", "mercado", "liga"])
        .agg(
            total_apostas=("id", "count"),
            greens=("green", "sum"),
            reds=("green", lambda x: (~x).sum()),
            media_confianca=("confianca", "mean"),
            roi=("retorno", lambda r: round((r.sum() - df["stake_usada"].sum()) / df["stake_usada"].sum() * 100, 2))
        )
        .reset_index()
    )

    resumo["acuracia"] = (resumo["greens"] / resumo["total_apostas"] * 100).round(2)
    resumo["data_ultima_atualizacao"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    resumo.to_sql("aprendizado_resultado", conn, if_exists="replace", index=False)
    conn.commit()
    conn.close()
    print("✅ Aprendizado contínuo atualizado com sucesso.")
