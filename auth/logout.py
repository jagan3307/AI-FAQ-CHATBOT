import streamlit as st


def logout_user():
    st.session_state.logged_in = False
    st.session_state.user = None
    st.session_state.messages = []
    st.session_state.chat_id = None

    st.rerun()