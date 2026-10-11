import pandas as pd

def qualite_binaire(note):
    if note >= 7:
        return "1"
    else:
        return "0"


def norm(df: pd.DataFrame) -> pd.DataFrame:
    return (df - df.mean()) / df.std()