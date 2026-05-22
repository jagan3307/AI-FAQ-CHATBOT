import streamlit as st
from database.user_db import login_user
from database.connection import supabase


def login_page():

    st.subheader("Login")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        user = login_user(
            email,
            password
        )

        if user:

            st.session_state.logged_in = True

            st.session_state.user = (
                user.id,
                user.email
            )

            st.success(
                "Login Successful"
            )

            st.rerun()

        else:
            st.error(
                "Invalid Credentials"
            )

    st.markdown("### OR")

    if st.button("🔵 Continue with Google"):

        response = supabase.auth.sign_in_with_oauth({
            "provider": "google",
            "options": {
                "redirect_to":
                "https://ai-faq-chatbot-007.streamlit.app/"
            }
        })

        st.link_button(
            "Continue with Google",
            response.url
        )