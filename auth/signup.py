import streamlit as st
from database.user_db import register_user


def signup_page():

    st.subheader("Create Account")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Signup"):

        user = register_user(
            email,
            password
        )

        if user:

            st.success(
                "Signup Successful"
            )

        else:
            st.error(
                "Signup Failed"
            )