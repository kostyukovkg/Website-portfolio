import streamlit as st
import pandas as pd

st.header('Python mini apps')
st.write('This page contains apps developed during my Python self study program.'
         '')

col1, empty_col1, col2 = st.columns([2.0, 0.2, 2.0])  # задаем отношение ширины разных колонок

df = pd.read_csv("data.csv", sep=';')  # чтение файла с данными

with col1:
    for index, row in df[:10].iterrows():  # метод итерации по строкам
        st.subheader(row['title'])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")  # special syntax for links

with col2:
    for index, row in df[10:].iterrows():
        st.subheader(row['title'])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")  # special syntax for links
