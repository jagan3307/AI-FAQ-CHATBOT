import streamlit as st
from database.connection import supabase


def signup_page():

    st.markdown(
        '<h1 class="main-title">🤖 AI FAQ Chatbot</h1>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p class="sub-title">Create your account</p>',
        unsafe_allow_html=True
    )

    st.markdown('<div class="auth-box">', unsafe_allow_html=True)

    st.subheader("Create Account")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Create Account"):

        try:

            supabase.auth.sign_up({
                "email": email,
                "password": password
            })

            st.success(
                "Account Created Successfully"
            )

        except Exception:
            st.error("Signup Failed")

    st.markdown('</div>', unsafe_allow_html=True)