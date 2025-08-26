import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
bmi = np.where(df['weight'] / ((df['height']/100)**2) > 25, 1, 0)
df['overweight'] = bmi

# 3
gluc = np.where(df['gluc'] > 1, 1, 0)
cholesterol = np.where(df['cholesterol'] > 1, 1, 0)
df['gluc'] = gluc
df['cholesterol'] = cholesterol


# 4
def draw_cat_plot():
    # 5
    df_cat = df.melt(id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    # 6
    df_cat = df_cat[['cardio', 'variable', 'value']].value_counts().reset_index().rename(columns={'count': 'total'})
    # 7
    # 8
    fig =     sns.catplot(data=df_cat, x='variable', y='total', hue='value', kind='bar', col='cardio')


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
    (df['height'] >= df['height'].quantile(0.025)) &
    (df['height'] < df['height'].quantile(0.975)) &
    (df['weight'] >= df['weight'].quantile(0.025)) &
    (df['weight'] < df['weight'].quantile(0.975))]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(corr)

    # 14
    fig, ax = plt.subplots(figsize=(12,12))

    # 15
    sns.heatmap(data=corr, annot=True, fmt='.1f', mask=mask, ax=ax, linewidths=.5)


    # 16
    fig.savefig('heatmap.png')
    return fig
