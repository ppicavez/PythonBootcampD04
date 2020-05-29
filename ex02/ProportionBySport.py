import pandas as pd


def proportionBySport(df, olympic_year, sport, gender):
    result = {}
    mask = (df["Year"] == olympic_year) & (df["Sex"] == gender)\
        & (df['Sport'] == sport)
    df_selected = df[mask]
    df_selected = df_selected.drop_duplicates(subset=['ID'])
    nb_selected = len(df_selected)
    print(nb_selected)

    mask = (df["Year"] == olympic_year) & (df["Sex"] == gender)
    df_selected = df[mask]
    df_selected = df_selected.drop_duplicates(subset=['ID'])
    nb_global_selected = len(df_selected)
    print(nb_global_selected)

    return nb_selected / nb_global_selected
