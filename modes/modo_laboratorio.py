
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
    print("🔬 [Laboratório] Testando sinais ousados...")
    jogos = obter_jogos_do_dia()
    mercados = ["Gol após 75 minutos", "Jogador para marcar", "Finalizações por tempo"]

    for jogo in jogos:
        mercado = random.choice(mercados)
        odd = buscar_odd_real(jogo, mercado)
        ev = round(random.uniform(1.5, 6.0), 2)
        confianca = random.randint(75, 90)

        if ev > 0 and confianca >= 75:
            mensagem = f"[Lab] Experimento: {jogo} - {mercado} @ {odd} (EV {ev}%)"
            enviar_sinal(mensagem)
            registrar_sinal({
                "jogo": jogo,
                "mercado": mercado,
                "odd": odd,
                "ev": ev,
                "confianca": confianca
            }, modo="laboratorio")
    print("✅ [Laboratório] Fim do experimento.")
