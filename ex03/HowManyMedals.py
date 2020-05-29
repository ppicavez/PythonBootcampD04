import pandas as pd


def howManyMedals(df, participant_name):
    result = {}
    df['Gold'] = df["Medal"] == 'Gold'
    df['Silver'] = df["Medal"] == 'Silver'
    df['Bronze'] = df["Medal"] == 'Bronze'

    mask = (df["Name"] == participant_name) 
    df_selected = df[mask]
    gb = df_selected.groupby('Year')
    result = gb['Gold','Silver','Bronze'].sum()
    for ind_ligne, contenu_ligne in result.iterrows():
        print("Voici le panda %s :" % ind_ligne)
        print(contenu_ligne)
        print("--------------------")
    return result[0]

