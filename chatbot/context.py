import streamlit as st

def set_pdf_context(text):
    st.session_state.pdf_context = text

def get_pdf_context():
    return st.session_state.get("pdf_context", "")