import streamlit as st
from database.user_db import register_user


def signup_page():
    st.subheader("Create Account")

    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Signup"):

        success = register_user(username, email, password)

        if success:
            st.success("Account Created")
        else:
            st.error("Username Already Exists")