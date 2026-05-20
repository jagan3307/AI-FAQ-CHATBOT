import streamlit as st


def display_messages(messages):

    for msg in messages:

        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])