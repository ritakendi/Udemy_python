import streamlit as st
from email_send import send_email
import pandas

df = pandas.read_csv("topics.csv")

with st.form(key="email_form"):
    user_email = st.text_input("Your Email Address")
    option = st.selectbox('What Topic do you want to discuss',
                          df["topic"])
    user_text = st.text_area("Text")

    text = f"""\
Subject: New Email from {user_email}

From: {user_email}
{user_text}
"""
    button = st.form_submit_button("Submit")

    if button:
        send_email(text)
        st.info("Your email was sent succesfully")
