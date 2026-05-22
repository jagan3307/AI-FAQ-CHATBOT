import streamlit as st
from database.connection import supabase


def login_page():

    st.subheader("Login")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    # =========================
    # EMAIL LOGIN (SUPABASE ONLY)
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
                st.session_state.user = (
                    user.id,
                    user.email
                )

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
                "redirect_to": "https://ai-faq-chatbot-007.streamlit.app/?code=431d381e-17a2-4a89-9a34-3254845ee916"
            }
        })

        # IMPORTANT: no link_button needed
        st.markdown(
            f'<a href="{response.url}" target="_self">👉 Continue with Google</a>',
            unsafe_allow_html=True
        )