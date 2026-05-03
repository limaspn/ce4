import pandas as pd
from app.model import prever_demanda
from app.rules import risco_perda, risco_ruptura, risco_margem, score_final, recomendacao

def gerar_previsoes():
    df = pd.read_csv("data/data.csv")
    produtos = df['produto'].unique()

    resultados = []

    for produto in produtos:
        df_prod = df[df['produto'] == produto].iloc[-1]

        estoque = df_prod['estoque']
        preco_venda = df_prod['preco_venda']
        preco_compra = df_prod['preco_compra']

        demanda_prevista = prever_demanda(df, produto)

        r_perda = risco_perda(estoque, demanda_prevista)
        r_ruptura = risco_ruptura(estoque, demanda_prevista)
        r_margem = risco_margem(preco_compra, preco_venda)

        score = score_final(r_perda, r_ruptura, r_margem)
        rec = recomendacao(r_perda, r_ruptura)

        resultados.append({
            "produto": str(produto),
            "demanda_prevista": float(round(demanda_prevista, 2)),
            "estoque": int(estoque),
            "score": float(round(score, 2)),
            "acao": str(rec)
        })

    return resultados