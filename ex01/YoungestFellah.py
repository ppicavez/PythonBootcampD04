import pandas as pd


def youngestFellah(df,olympic_year):
    result = {}
    mask = (df["Year"] == olympic_year) & (df["Sex"] == 'M')
    df_selected =df[mask]
    result['m'] = df_selected['Age'].min()

    mask = (df["Year"] == olympic_year) & (df["Sex"] == 'F')
    df_selected =df[mask]
    result['f'] = df_selected['Age'].min()
    
    return result
