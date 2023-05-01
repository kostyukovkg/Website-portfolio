import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

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
"""
st.write(content2)

col3, empty_col, col4 = st.columns([2.0, 0.3, 2.0]) # задаем отношение ширины разных колонок

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
