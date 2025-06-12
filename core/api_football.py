
import random

USE_REAL_API = False  # Troque para True se quiser usar a API-Football real

def obter_jogos_do_dia():
    if USE_REAL_API:
        # Aqui entraria a lógica real com requests e sua API key
        raise NotImplementedError("Integração com API-Football ainda não implementada.")
    else:
        # Simulação
        times = ["Santos", "Palmeiras", "Flamengo", "Corinthians", "Atlético-MG", "Grêmio", "Inter", "São Paulo", "Botafogo", "Fluminense"]
        jogos = []
        for _ in range(random.randint(5, 10)):
            a, b = random.sample(times, 2)
            jogos.append(f"{a} x {b}")
        return jogos
