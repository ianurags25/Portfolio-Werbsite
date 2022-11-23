import streamlit
from send_mail import send_email
streamlit.header("Contact Me")

with streamlit.form(key = "email_forms"):
    user_email = streamlit.text_input("Your Email Address")
    raw_message = streamlit.text_area("Your Message")
    message = f"""\
Subject:New email from {user_email}
From: {user_email}
{raw_message}
"""
    button = streamlit.form_submit_button("Submit!")
    if button:
        send_email(message)
        streamlit.info("Your email was sent successfully")
