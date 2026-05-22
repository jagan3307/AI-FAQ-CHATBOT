import streamlit as st
from urllib.parse import urlparse, parse_qs

from auth.login import login_page
from auth.signup import signup_page
from auth.logout import logout_user

from ui.sidebar import sidebar
from ui.chat_ui import display_messages
from ui.styles import load_css

from utils.session import init_session

from chatbot.pdf_loader import extract_text_from_pdf
from chatbot.context import set_pdf_context

from chatbot.response_handler import get_bot_response

from database.chat_db import create_chat
from database.message_db import save_message

from chatbot.faq_generator import generate_faqs_from_idea
from chatbot.dynamic_faq import parse_faqs

from database.connection import supabase


# ================================
# PAGE CONFIG
# ================================
st.set_page_config(
    page_title="AI FAQ Chatbot",
    page_icon="🤖",
    layout="wide"
)

init_session()
load_css()


# ================================
# INITIAL STATE
# ================================
st.session_state.setdefault("logged_in", False)
st.session_state.setdefault("messages", [])
st.session_state.setdefault("chat_id", None)
st.session_state.setdefault("theme", "light")


# =========================================================
# 🔥 OAUTH FIX (MUST BE AT TOP BEFORE LOGIN CHECK)
# =========================================================
query_params = st.query_params

if "code" in query_params:

    try:
        code = query_params["code"]

        session = supabase.auth.exchange_code_for_session(code)

        if session and session.session:

            user = session.session.user

            st.session_state.logged_in = True
            st.session_state.user = (user.id, user.email)

            # clean URL
            st.query_params.clear()

            st.rerun()

    except Exception as e:
        st.error("Google login failed")
        st.exception(e)


# ================================
# SESSION RESTORE (NORMAL LOGIN)
# ================================
try:
    session = supabase.auth.get_session()

    if session and session.session:

        user = session.session.user

        st.session_state.logged_in = True
        st.session_state.user = (user.id, user.email)

except Exception:
    pass


# ================================
# TITLE
# ================================
st.title("🤖 AI FAQ Chatbot")


# ================================
# LOGIN / SIGNUP PAGE
# ================================
if not st.session_state.logged_in:

    menu = st.sidebar.selectbox(
        "Menu",
        ["Login", "Signup"]
    )

    if menu == "Login":
        login_page()

    else:
        signup_page()


# ================================
# MAIN APP
# ================================
else:

    user_id = st.session_state.user[0]

    sidebar(user_id)

    # THEME
    if st.sidebar.button("🌙 Toggle Dark/Light Mode"):

        st.session_state.theme = (
            "dark"
            if st.session_state.theme == "light"
            else "light"
        )

        st.rerun()

    # LOGOUT
    if st.sidebar.button("Logout"):

        supabase.auth.sign_out()
        logout_user()

    # HEADER
    st.subheader("🤖 AI FAQ Assistant")

    # BUSINESS FAQ
    use_business_faq = st.checkbox("💡 Use Business Idea FAQ Generator")

    if use_business_faq:

        idea = st.text_area("Enter your business / college idea")

        if st.button("Generate FAQs"):

            if idea:

                faq_text = generate_faqs_from_idea(idea)

                st.session_state.dynamic_faqs = parse_faqs(faq_text)

                st.success("FAQs Generated Successfully 🚀")

            else:
                st.warning("Please enter an idea")

        if "dynamic_faqs" in st.session_state:

            st.subheader("📋 Generated FAQs")

            for faq in st.session_state.dynamic_faqs:

                st.markdown(f"**Q:** {faq['question']}")
                st.markdown(f"**A:** {faq['answer']}")
                st.divider()

    # PDF UPLOAD
    use_pdf = st.checkbox("📄 Use PDF Knowledge Base")

    if use_pdf:

        pdf_file = st.file_uploader("Upload PDF", type=["pdf"])

        if pdf_file is not None:

            text = extract_text_from_pdf(pdf_file)

            set_pdf_context(text[:12000])

            st.success("PDF Loaded Successfully!")

    # CHATBOT
    st.subheader("💬 AI Chatbot")

    display_messages(st.session_state.messages)

    prompt = st.chat_input("Ask your questions...")

    if prompt:

        st.session_state.messages.append({
            "role": "user",
            "content": prompt
        })

        with st.chat_message("user"):
            st.markdown(prompt)

        if st.session_state.chat_id is None:

            title = prompt[:30]

            chat_id = create_chat(user_id, title)

            st.session_state.chat_id = chat_id

        save_message(st.session_state.chat_id, "user", prompt)

        with st.chat_message("assistant"):

            reply = get_bot_response(prompt, st.session_state.messages)

            st.markdown(reply)

        st.session_state.messages.append({
            "role": "assistant",
            "content": reply
        })

        save_message(st.session_state.chat_id, "assistant", reply)