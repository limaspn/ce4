import pandas as pd

def prever_demanda(df: pd.DataFrame, produto: str) -> float:
    df_prod = df[df['produto'] == produto]
    return df_prod['quantidade_vendida'].mean()