import streamlit as st
import pandas as pd

# st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Konstantin Kostyukov")
    content = """
    Write smth
    """
    # st.write(content)
    st.info(content)

content2 = """
Здание администрации парка Горького в Москве (улица Крымский Вал 9, строение 45) — 
историческое здание в северном углу парка, примыкающее к Крымскому мосту 
и выходящее западным фасадом на Пушкинскую набережную. 
В его основе — Т-образный в плане цех судостроительного завода «Крымский Бромлей», 
построенный в 1893—1895 годы по проекту С. В. Шервуда[⇨]. 
В 1923 году цех был перестроен в павильон Всероссийской выставки[⇨], в 1931—1934 годы — 
в трёхэтажный административный корпус со звуковым кинотеатром на 1500 зрителей[⇨]. 
В проектировании и художественном оформлении участвовали 
А. В. Власов, А. А. Дейнека, Л. С. Залесская, Л. М. Лисицкий, А. В. Щусев, братья Пашковы, братья Стенберги и многие другие мастера.
В 1942 году прямое попадание авиабомбы уничтожило зрительный зал кинотеатра, но его внешние стены устояли. 
С тех пор в течение более восьмидесяти лет здание существует как два обособленных объёма, 
между которыми находятся не видимые с улицы руины.
"""
st.write(content2)

col3, empty_col, col4 = st.columns([2.0, 0.5, 2.0]) # задаем отношение ширины разных колонок

df = pd.read_csv("data.csv", sep=';')  # чтение файла с данными

with col3:
    for index, row in df[:10].iterrows():  # метод итерации по строкам
        st.header(row['title'])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write("[Source Code](https://pythonhow.com)")  # special syntaxis for links

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")  # special syntaxis for links
