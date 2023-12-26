import streamlit as st
from send_email import send_email

st.header('Contact Me')

with st.form(key="main_form"):
    user_name = st.text_input("Please introduce yourself")
    user_email = st.text_input("Please enter your email address and I will reply to you")
    raw_message = st.text_area("Please enter your message to me here")  # Allows to enter a multiple line message
    message = f"""\
    Subject: New email from web site from: {user_email}

    {raw_message}    
    
    From: {user_name}
    {user_email}
    """

    button = st.form_submit_button('Send email')  # special button that submits text for the form.
    # text can be sent to a database or by email etc.
    if button:
        send_email(message)
        st.info("Your email was sent successfully")
