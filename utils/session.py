import streamlit as st


def init_session():
    if "theme" not in st.session_state:
        st.session_state.theme = "light"
        
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if "user" not in st.session_state:
        st.session_state.user = None

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "chat_id" not in st.session_state:
        st.session_state.chat_id = None