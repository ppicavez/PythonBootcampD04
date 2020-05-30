import pandas as pd


def howManyMedalsByCountry(df, country):
    result = {}
    df['Gold'] = df["Medal"] == 'Gold'
    df['Silver'] = df["Medal"] == 'Silver'
    df['Bronze'] = df["Medal"] == 'Bronze'

    mask = (df["Team"] == country)
    df_selected = df[mask]
    gb = df_selected.groupby('Year')
    calcul = gb['Gold', 'Silver', 'Bronze'].sum()
    for ind_ligne, contenu_ligne in calcul.iterrows():
        medals = {}
        medals['G'] = contenu_ligne[0]
        medals['S'] = contenu_ligne[1]
        medals['B'] = contenu_ligne[2]
        result[ind_ligne] = medals

    return result
