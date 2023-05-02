import streamlit as st

st.header('Contact Me')

with st.form(key="main_form"):
    user_email = st.text_input("Enter your email adress")
    message = st.text_area("Enter your message to me here")  # Allows to enter a multiple line message
    button = st.form_submit_button()  # special button that submits text for the form.
        # text can be sent to a database or by email etc.
    
