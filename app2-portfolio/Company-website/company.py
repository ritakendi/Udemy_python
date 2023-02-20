import streamlit as st
import pandas

# set webpage layout to wide
st.set_page_config(layout="wide")

# Add a header and some text
st.header("The Best Company")
description = """
        XYZ Tech is a cutting-edge technology company that offers innovative solutions to various industries.
        From software development and AI to cloud computing and cybersecurity,
        our team of skilled experts delivers quality services to clients all around the world.
        With a focus on providing efficient, cost-effective, and tailored solutions, 
        we aim to transform the way businesses operate and help them achieve their goals faster.
        At XYZ Tech, we are committed to excellence and continuously strive to push the boundaries of what's possible.
"""
st.write(description)
st.subheader("Our Team")

# columns
col1, col2, col3 = st.columns(3)

df = pandas.read_csv("data.csv")

col1, empty_col1, col2, empty_col2, col3 = st.columns(
    [9.5, 0.5, 11.5, 0.5, 12.5])


with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image('images/' + row['image'])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image('images/' + row['image'])

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image('images/' + row['image'])
