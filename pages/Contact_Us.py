import streamlit as st
import pandas
from send_email import send_email

data = pandas.read_csv("topics.csv")
topics = data['topic'].tolist()


with st.form("Email", clear_on_submit=True):
    user_email = st.text_input("Enter Your Email")

    Topic = st.selectbox("What Topic would you like to Discuss?",
                         topics)

    raw_message = st.text_area("message")

    message = f"""\
Subject: New email from {user_email}

From: {user_email}
Topic: {Topic}

{raw_message}
"""

    if st.form_submit_button("Submit"):
        send_email(message)
        st.info("Email Sent Successfully")
