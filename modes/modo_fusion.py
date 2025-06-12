
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
    print("🔍 [Fusion] Iniciando busca por sinais...")
    jogos = obter_jogos_do_dia()
    mercados = ["Mais de 2.5 gols", "Ambos Marcam", "Resultado + Over 1.5"]

    for jogo in jogos:
        mercado = random.choice(mercados)
        odd = buscar_odd_real(jogo, mercado)
        prob_real = estimar_probabilidade_real(jogo, mercado)
        ev = calcular_ev(prob_real, odd)
        confianca = int(prob_real * 100)

        if confianca >= 85 and ev > 0:
            mensagem = f"[Fusion] Aposta: {jogo} - {mercado} @ {odd} (EV {ev}%)"
            enviar_sinal(mensagem)
            registrar_sinal({
                "jogo": jogo,
                "mercado": mercado,
                "odd": odd,
                "ev": ev,
                "confianca": confianca
            }, modo="fusion")
    print("✅ [Fusion] Fim da análise.")
