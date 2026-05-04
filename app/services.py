import pandas as pd
from app.model import prever_demanda
from app.rules import risco_perda, risco_ruptura, risco_margem, score_final, recomendacao


def gerar_previsoes():
    df = pd.read_csv("data/data.csv")

    produtos = df["produto"].unique()

    resultados = []

    for produto in produtos:
        # pega última linha do produto (estado atual)
        df_prod_all = df[df["produto"] == produto]
        df_prod = df_prod_all.iloc[-1]

        estoque = df_prod["estoque"]
        preco_venda = df_prod["preco_venda"]
        preco_compra = df_prod["preco_compra"]

        # 🔥 PREVISÃO (EMA + dia da semana)
        demanda_prevista = prever_demanda(df, produto)

        # 🔥 MÉTRICAS DE ESTOQUE
        excesso = estoque - demanda_prevista
        falta = max(demanda_prevista - estoque, 0)

        # 🔥 MÉTRICAS FINANCEIRAS
        # perda = produto parado / risco de estragar
        perda = max(excesso, 0) * preco_compra

        # margem unitária
        margem = preco_venda - preco_compra

        # oportunidade = deixou de vender
        oportunidade = falta * margem

        # 🔥 RISCOS (mantém lógica existente)
        r_perda = risco_perda(estoque, demanda_prevista)
        r_ruptura = risco_ruptura(estoque, demanda_prevista)
        r_margem = risco_margem(preco_compra, preco_venda)

        score = score_final(r_perda, r_ruptura, r_margem)

        # 🔥 RECOMENDAÇÃO BASEADA NO HISTÓRICO
        rec = recomendacao(estoque, demanda_prevista)

        resultados.append({
            "produto": str(produto),
            "demanda_prevista": float(round(demanda_prevista, 2)),
            "estoque": int(estoque),
            "excesso": float(round(excesso, 2)),
            "perda": float(round(perda, 2)),
            "oportunidade": float(round(oportunidade, 2)),
            "score": float(round(score, 2)),
            "acao": str(rec)
        })

    return resultados