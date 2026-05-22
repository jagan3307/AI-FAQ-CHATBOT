import streamlit as st
from database.connection import supabase


def login_page():

    st.subheader("Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    # =========================
    # EMAIL LOGIN
    # =========================
    if st.button("Login"):

        try:
            response = supabase.auth.sign_in_with_password({
                "email": email,
                "password": password
            })

            user = response.user

            if user:
                st.session_state.logged_in = True
                st.session_state.user = (user.id, user.email)

                st.success("Login Successful")
                st.rerun()

        except Exception as e:
            st.error("Login Failed")
            st.exception(e)

    st.markdown("### OR")

    # =========================
    # GOOGLE LOGIN (FIXED)
    # =========================
    if st.button("🔵 Continue with Google"):

        response = supabase.auth.sign_in_with_oauth({
            "provider": "google",
            "options": {
                # MUST be your deployed app URL (NO CODE HERE)
                "redirect_to": "https://ai-faq-chatbot-007.streamlit.app/"
            }
        })

        # redirect user properly
        st.markdown(
            f'<meta http-equiv="refresh" content="0; url={response.url}">',
            unsafe_allow_html=True
        )