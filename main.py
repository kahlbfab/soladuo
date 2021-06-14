import streamlit as st
import pandas as pd
import plotly.express as px


def load_preprocess(path):
    df = pd.read_csv(path, encoding='latin1')
    df.drop(['Phone'], axis = 1, inplace = True)
    df.sort_values(by=['Team', 'Kategorie'], inplace=True)
    df.reset_index(drop=True, inplace=True)
    df.index += 1

    return df


def fig_category_bar_plot(df):
    df_plot = df[['Kategorie', 'Name']].groupby(['Kategorie']).agg('count').reset_index()
    df_plot.rename(columns={'Name': 'Anzahl'}, inplace=True)
    fig = px.bar(df_plot, x='Kategorie', y='Anzahl', title='Kategorien')
    return fig


def fig_lottery_pie_plot(df):
    df_plot = df[['Team_lotterie', 'Name']].groupby(['Team_lotterie']).agg('count').reset_index()
    df_plot.rename(columns={'Name': 'Anzahl'}, inplace=True)
    fig = px.pie(df_plot, values='Anzahl', names='Team_lotterie',
                    title='Teampartner Auslosen?',
                    color='Team_lotterie',
                    color_discrete_map={'Ja': px.colors.qualitative.Set3[6],
                                        'egal': px.colors.qualitative.Pastel[4],
                                        'Nein': px.colors.qualitative.Plotly[1]})
    return fig

info_text = '''
Csaba und Ich (Fabian) hatten das Ziel diesen Sommer am Sola Duo Lauf teilzunehmen, da dieser nun abgesagt ist,
 planen wir einen ähnlichen Lauf selbständig durchzuführen.

Wir werden nichts Grosses planen, sondern nur der grobe Rahmen organisieren. Es ist kein Wettkampf,
 sondern nur eine Challenge für sich selbst.

- Viele gute Tipps und Infos gibt es auf der Website zum orginalen [Sola Duo Lauf](https://www.asvz.ch/event/59394-sola-duo) 
- Konkretere Informationen werden noch folgen

---

**Modus:** 
Im Zweierteam wird die rund 65 - 75 km lange Strecke von Sargans oder Bad Ragaz nach Tann gemeinsam bewältigt:
 eine/r fährt Velo, der/die andere läuft. Im Team darf beliebig oft gewechselt werden, wobei der Velofahrer
  stets den Läufer eng begleiten muss.

**Datum:**
**25.09.21**, Verschiebungsdatum 02.10.21

**Ablauf:**
- Gepäck Depot bei Sheryl Ludescher ein paar Tage vor dem Lauf oder am frühen Morgen des Laufes selbst. 
Adresse - Erikastrasse 5 8632 Tann ZH
- Gemeinsame Reise mit dem Zug: Rüti -> Sargans oder Bad Ragaz

**Laufstrecke:**
Ist noch nicht ganz entschieden, [hier](https://onthegomap.com/s/kqdq1isg) eine grobe Version von Sargans nach Tann:
Der Lauf endet bei Sheryl Ludescher zuhause. Dort kann man evlt. noch etwas kleines essen.  
'''


df_regist = load_preprocess("data/registrations.csv")

st.title('Sola Duo / Trio September 2021')

st.header('Infos')
st.markdown(info_text)

st.header('Teilnehmer')
st.write(df_regist)

st.plotly_chart(fig_category_bar_plot(df_regist), use_container_width=True)









