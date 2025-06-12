
# core/telegram_sender.py
import requests

BOT_TOKEN = "7590925126:AAFiCWBAFfztEm_EqLoU2QibTfYkndPhv9M"
CHAT_ID = "1146864652"

def enviar_sinal(texto):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": texto,
        "parse_mode": "HTML"
    }
    try:
        response = requests.post(url, data=payload)
        if response.status_code != 200:
            print("Erro ao enviar mensagem:", response.text)
    except Exception as e:
        print("Exceção ao tentar enviar mensagem:", e)
