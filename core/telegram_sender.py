import requests

TOKEN = "7590925126:AAFiCWBAFfztEm_EqLoU2QibTfYkndPhv9M"
CHAT_ID = "1146864652"

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
