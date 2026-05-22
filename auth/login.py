import streamlit as st
from database.connection import supabase


def login_page():

    st.markdown(
        '<h1 class="main-title">🤖 AI FAQ Chatbot</h1>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p class="sub-title">AI Assistant with Google Authentication</p>',
        unsafe_allow_html=True
    )

    st.markdown('<div class="auth-box">', unsafe_allow_html=True)

    st.subheader("Login")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        try:

            response = supabase.auth.sign_in_with_password({
                "email": email,
                "password": password
            })

            user = response.user

            st.session_state.logged_in = True
            st.session_state.user = (
                user.id,
                user.email
            )

            st.success("Login Successful")

            st.rerun()

        except Exception:
            st.error("Invalid Email or Password")

    st.markdown("### OR")

    if st.button("🔵 Continue with Google"):

        response = supabase.auth.sign_in_with_oauth({
            "provider": "google"
        })

        st.link_button(
            "Open Google Login",
            response.url
        )

    st.markdown('</div>', unsafe_allow_html=True)