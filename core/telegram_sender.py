import requests

TOKEN = "7590925126:AAFiCWBAFfztEm_EqLoU2QibTfYkndPhv9M"
CHAT_ID = "1146864652"

def enviar_telegram(mensagem):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {'chat_id': CHAT_ID, 'text': mensagem}
    requests.post(url, data=data)