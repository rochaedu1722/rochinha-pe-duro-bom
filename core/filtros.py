def calcular_ev_kelly(prob, odd):
    ev = prob * (odd - 1) - (1 - prob)
    kelly = (prob * (odd - 1) - (1 - prob)) / (odd - 1)
    return ev, round(max(min(kelly, 1), 0), 2)