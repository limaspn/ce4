def risco_perda(estoque, demanda_prevista):
    if estoque == 0:
        return 0
    return (estoque - demanda_prevista) / estoque

def risco_ruptura(estoque, demanda_prevista):
    if demanda_prevista == 0:
        return 0
    return (demanda_prevista - estoque) / demanda_prevista

def risco_margem(preco_compra, preco_venda):
    if preco_venda == 0:
        return 0
    return preco_compra / preco_venda

def score_final(r_perda, r_ruptura, r_margem):
    return (0.5 * r_perda) + (0.3 * r_ruptura) + (0.2 * r_margem)

def recomendacao(r_perda, r_ruptura):
    if r_perda > 0.3:
        return "Reduzir preço / evitar compra"
    elif r_ruptura > 0.3:
        return "Comprar mais urgente"
    else:
        return "Estoque saudável"