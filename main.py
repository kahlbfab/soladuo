import streamlit as st
import pandas as pd
import plotly.express as px


def load_preprocess(path):
    df = pd.read_csv(path, encoding='latin1')
    df.drop(['Mobile_Nummer'], axis=1, inplace=True)
    df.sort_values(by=['Kategorie', 'Team'], inplace=True)
    df.reset_index(drop=True, inplace=True)
    df.index += 1

    return df


def fig_category_bar_plot(df):
    df_plot = df[['Kategorie', 'Name']].groupby(['Kategorie']).agg('count').reset_index()
    df_plot.rename(columns={'Name': 'Anzahl'}, inplace=True)
    fig = px.bar(df_plot, x='Kategorie', y='Anzahl', title='Kategorien')
    return fig


info_text = '''
Csaba und Ich (Fabian) hatten das Ziel diesen Sommer am Sola Duo Lauf teilzunehmen, da dieser nun abgesagt ist,
 planen wir einen ähnlichen Lauf selbständig durchzuführen.

- Viele gute Tipps und Infos gibt es auf der Website zum orginalen [Sola Duo Lauf](https://www.asvz.ch/event/59394-sola-duo) 
- Detailierter Erfahrungsbericht [hier](https://tomholzweg.jimdo.com/berichte/35-bericht-sola-duo-mit-erich-kunz-21-06-2019/)

---

**Modus** 
Im Zweierteam wird die rund 61.3 km lange Strecke von Sargans nach Tann gemeinsam bewältigt:
 eine/r fährt Velo, der/die andere läuft. Im Team darf beliebig oft gewechselt werden, wobei der Velofahrer
  stets den Läufer eng begleiten muss.

**Datum**
**25.09.21 (Start: am frühen Morgen)**, Verschiebungsdatum 02.10.21

**Ablauf**
- Gepäck Depot (Duschsachen, Kleider zum Umziehen) bei Sheryl Ludescher ein paar Tage vor dem Lauf oder am frühen Morgen des Laufes selbst. 
Adresse - Erikastrasse 5 8632 Tann ZH am besten mit Sheryl Ludescher 078 976 14 02 absprechen. 
- Gemeinsame Reise mit dem Zug: 0624 ab Rüti -> 0723 in Sargans
- **Start: ca. 0745 in Sargans** 
- Ziel: In Tann bei Sheryl Ludescher Zuhause. Dort kann man duschen und es wird noch Apero und etwas kleines zu Essen geben, falls man Lust hat. 

**Laufstrecke**
- [Strecke OnTheGoMap](https://onthegomap.com/s/lkvkk7kj). Die Strecke muss nicht immer 100% eingehalten werden, aber probiert es möglichst gut. 
  Die Strecke ist relativ einfach, da meistens einem Veloweg gefolgt werden kann neben einem Fluss/See. 2/3 ist Teer und 1/3 Kies. Auf der Karte
  (onthegomap) sieht man auch den eigenen Standort und kann diese somit auch während des Laufes benutzen.
- Verpflegunsposten 1 Kilometer 33: Nach dem Walensee bei Wesen [ungefährer Standort](https://goo.gl/maps/dWVA3XispmkbqLAx5)
- Verpflegunsposten 2 Kilometer 48: Bei der Badi in Grynau [ungefährer Standort](https://goo.gl/maps/V7FQbBqBUDsvpBG1A)

**Helfer**

Name | Info | Telefon Nummer für Notfälle
-------- | -------- | --------
Thomas Hari | Fährt mit E-Bike Strecke ab und hat Veloflickzeug dabei | 079 643 78 70
Julia Hari  | Verpfelungsposten 1 |  079 751 35 24
Familie Roth  | Verpflegungsposten 2 |  079 546 89 09


**Empfehlung Packliste**
- Verpflegung: Nehmt am besten alles mit was ihr für den ganzen Lauf benötigt. An den Verpflegungsständen wird es Banane und Bouillon oder Isostar geben. Brunnen hat es einige entlang der Strecke.  
- Ersatzreifen (Velo Flickzeug hat Thomas Hari)
- Verbandsmaterial
- Mind. 1 Handy pro Team für Notfälle
'''


df_regist = load_preprocess("data/soladuo_teilnehmer.csv")

st.title('Sola Duo / Trio September 2021')

st.header('Infos')
st.markdown(info_text)

st.header('Teilnehmer')
st.dataframe(df_regist, height=550)
#st.write(df_regist)

#st.plotly_chart(fig_category_bar_plot(df_regist), use_container_width=True)









