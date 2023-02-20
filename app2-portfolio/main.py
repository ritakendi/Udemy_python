import streamlit as st
import pandas


st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Kendi Rita")
    content = """
            My name is Kendi and I'm a tech enthusiast, problem-solver, and software developer with a burning passion for all things programming.
            I have been fortunate enough to spend a year honing my skills as a programmer at the prestigious ALX-Holberton school,
            where I was able to work on exciting projects and develop my expertise in cutting-edge technologies. 
            Whether it's building web applications or designing algorithms, 
            I thrive on the challenge of creating innovative solutions that can make a real difference in people's lives.
            
        """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in python.Feel free to contact me!
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])


df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
