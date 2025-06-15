
import os
import requests
from dotenv import load_dotenv
from core.aprendizado import sinal_ja_enviado, registrar_sinal_enviado

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def enviar_telegram(mensagem):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {'chat_id': CHAT_ID, 'text': mensagem}

    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print("✅ Mensagem enviada com sucesso ao Telegram.")
        else:
            print(f"❌ Erro ao enviar mensagem: {response.status_code}")
            print(f"🧾 Detalhes: {response.text}")
    except Exception as e:
        print(f"❌ Erro inesperado ao enviar mensagem: {e}")

def enviar_telegram_sinal(sinal, modo, mensagem):
    jogo = sinal.get("jogo", "")
    mercado = sinal.get("mercado", "")
    odd = sinal.get("odd", 0)

    if sinal_ja_enviado(jogo, mercado, odd):
        print(f"🚫 Sinal repetido detectado: {jogo} | {mercado} | {odd}. Ignorado.")
        return

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {'chat_id': CHAT_ID, 'text': mensagem}

    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print("✅ Mensagem enviada com sucesso ao Telegram.")
            registrar_sinal_enviado(jogo, mercado, odd)
        else:
            print(f"❌ Erro ao enviar mensagem: {response.status_code}")
            print(f"🧾 Detalhes: {response.text}")
    except Exception as e:
        print(f"❌ Erro inesperado ao enviar mensagem: {e}")
