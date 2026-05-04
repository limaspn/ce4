import pandas as pd

def prever_demanda(df: pd.DataFrame, produto: str, alpha=0.4) -> float:
    # garantir formato de data
    df['data'] = pd.to_datetime(df['data'])

    # criar coluna de dia da semana
    df['dia_semana'] = df['data'].dt.dayofweek

    # pegar hoje
    hoje = pd.Timestamp.today().dayofweek

    # filtrar produto + dia da semana
    df_prod = df[
        (df['produto'] == produto) &
        (df['dia_semana'] == hoje)
    ]

    # fallback (se não tiver histórico suficiente)
    if df_prod.empty:
        df_prod = df[df['produto'] == produto]

    vendas = df_prod['quantidade_vendida'].tolist()

    if not vendas:
        return 0

    # EMA
    ema = vendas[0]

    for venda in vendas[1:]:
        ema = alpha * venda + (1 - alpha) * ema

    return ema