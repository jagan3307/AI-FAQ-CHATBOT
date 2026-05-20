import streamlit as st

def load_css():

    theme = st.session_state.get("theme", "light")

    if theme == "dark":

        st.markdown("""
        <style>

        /* ================= APP BACKGROUND ================= */
        .stApp {
            background-color: #0b1220;
            color: #ffffff;
        }

        /* ================= SIDEBAR ================= */
        section[data-testid="stSidebar"] {
            background-color: #0f172a;
        }

        /* ================= SIDEBAR LABEL (MENU) ================= */
        section[data-testid="stSidebar"] label {
            color: #ffffff !important;
        }

        /* ================= SELECTBOX MAIN TEXT ================= */
        section[data-testid="stSidebar"] [data-baseweb="select"] {
            color: #ffffff !important;
        }

        section[data-testid="stSidebar"] [data-baseweb="select"] * {
            color: #ffffff !important;
        }

        /* ================= DROPDOWN OPTIONS ================= */
        div[role="listbox"] div {
            color: #ffffff !important;
        }

        div[role="option"] {
            color: #ffffff !important;
        }

        /* Hover effect */
        div[role="option"]:hover {
            background-color: #374151 !important;
            color: #ffffff !important;
        }

        /* ================= HEADINGS ================= */
        h1, h2, h3, h4, h5, h6 {
            color: #ffffff !important;
        }

        /* ================= GENERAL TEXT ================= */
        p, span, label, div {
            color: #e5e7eb !important;
        }

        /* ================= INPUT BOXES ================= */
        input, textarea {
            background-color: #111827 !important;
            color: #ffffff !important;
            border: 1px solid #374151 !important;
            border-radius: 10px !important;
        }

        /* ================= CHAT INPUT ================= */
        .stChatInput input {
            background-color: #111827 !important;
            color: #ffffff !important;
        }

        /* ================= BUTTONS ================= */
        .stButton button {
            background-color: #4f46e5;
            color: white;
            border-radius: 10px;
            border: none;
            padding: 0.5rem 1rem;
            font-weight: 600;
            transition: 0.2s;
        }

        .stButton button:hover {
            background-color: #6366f1;
            transform: scale(1.02);
        }

        /* ================= CHAT MESSAGES ================= */
        .stChatMessage {
            background-color: #111827;
            border-radius: 10px;
            padding: 10px;
        }

        </style>
        """, unsafe_allow_html=True)

    else:

        st.markdown("""
        <style>

        /* ================= APP BACKGROUND ================= */
        .stApp {
            background-color: #ffffff;
            color: #111111;
        }

        /* ================= SIDEBAR ================= */
        section[data-testid="stSidebar"] {
            background-color: #1f2937;
        }

        /* ================= SIDEBAR LABEL (MENU) ================= */
        section[data-testid="stSidebar"] label {
            color: #ffffff !important;
        }

        /* ================= SELECTBOX MAIN TEXT ================= */
        section[data-testid="stSidebar"] [data-baseweb="select"] {
            color: #ffffff !important;
        }

        section[data-testid="stSidebar"] [data-baseweb="select"] * {
            color: #ffffff !important;
        }

        /* ================= DROPDOWN OPTIONS ================= */
        div[role="listbox"] div {
            color: #ffffff !important;
        }

        div[role="option"] {
            color: #ffffff !important;
        }

        div[role="option"]:hover {
            background-color: #374151 !important;
            color: #ffffff !important;
        }

        /* ================= HEADINGS ================= */
        h1, h2, h3, h4, h5, h6 {
            color: #111111 !important;
        }

        /* ================= GENERAL TEXT ================= */
        p, span, label, div {
            color: #111111 !important;
        }

        /* ================= INPUT BOXES ================= */
        input, textarea {
            background-color: #ffffff !important;
            color: #111111 !important;
            border: 1px solid #d1d5db !important;
            border-radius: 10px !important;
        }

        /* ================= CHAT INPUT ================= */
        .stChatInput input {
            background-color: #ffffff !important;
            color: #111111 !important;
        }

        /* ================= BUTTONS ================= */
        .stButton button {
            background-color: #2563eb;
            color: white;
            border-radius: 10px;
            border: none;
            padding: 0.5rem 1rem;
            font-weight: 600;
            transition: 0.2s;
        }

        .stButton button:hover {
            background-color: #1d4ed8;
            transform: scale(1.02);
        }

        /* ================= CHAT MESSAGES ================= */
        .stChatMessage {
            background-color: #f3f4f6;
            border-radius: 10px;
            padding: 10px;
        }

        </style>
        """, unsafe_allow_html=True)