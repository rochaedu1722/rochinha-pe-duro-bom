
from core.telegram_sender import enviar_sinal
from core.aprendizado import registrar_sinal
from core.api_football import obter_jogos_do_dia
from core.odd_scraper import buscar_odd_real
import random


def calcular_ev(prob_real, odd):
    """
    Calcula o Valor Esperado (Expected Value) com base em probabilidade real e odd.
    """
    return round((prob_real * odd) - (1 - prob_real), 2)


def estimar_probabilidade_real(jogo, mercado):
    """
    Estimar a probabilidade real de um mercado usando lógica simples ou aprendizado.
    Substituir por IA ou heurística mais precisa futuramente.
    """
    # Simulação básica — pode ser conectada ao histórico no futuro
    if "Mais de 2.5" in mercado:
        return 0.65
    elif "Ambos Marcam" in mercado:
        return 0.60
    elif "Resultado + Over" in mercado:
        return 0.55
    return 0.50


def executar():
    print("🔍 [Precision] Avaliando fair odds e EV...")
    jogos = obter_jogos_do_dia()
    mercados = ["Resultado + Over 1.5", "Dupla + Over 2.5", "Ambos Marcam"]

    for jogo in jogos:
        mercado = random.choice(mercados)
        odd_real = buscar_odd_real(jogo, mercado)
        odd_justa = round(odd_real - random.uniform(0.1, 0.3), 2)
        ev = round(((odd_real - odd_justa) / odd_justa) * 100, 2)
        confianca = random.randint(85, 95)

        if ev > 0 and confianca >= 85:
            mensagem = f"[Precision] Sinal: {jogo} - {mercado} @ {odd_real} (EV {ev}%)"
            enviar_sinal(mensagem)
            registrar_sinal({
                "jogo": jogo,
                "mercado": mercado,
                "odd": odd_real,
                "ev": ev,
                "confianca": confianca
            }, modo="precision")
    print("✅ [Precision] Fim da análise.")
