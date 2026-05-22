import streamlit as st

def load_css():

    theme = st.session_state.get("theme", "dark")

    if theme == "dark":

        st.markdown("""
        <style>

        .stApp {
            background: linear-gradient(
                135deg,
                #0f172a,
                #020617
            );
            color: white;
        }

        section[data-testid="stSidebar"] {
            background: #081028;
            border-right: 1px solid #1e293b;
        }

        .main-title {
            text-align: center;
            font-size: 52px;
            font-weight: 700;
            color: white;
            margin-bottom: 10px;
        }

        .sub-title {
            text-align: center;
            color: #94a3b8;
            margin-bottom: 40px;
            font-size: 18px;
        }

        .auth-box {
            background: rgba(15, 23, 42, 0.75);
            padding: 40px;
            border-radius: 22px;
            backdrop-filter: blur(12px);
            border: 1px solid #334155;
            max-width: 520px;
            margin: auto;
            margin-top: 30px;
            box-shadow: 0 8px 30px rgba(0,0,0,0.35);
        }

        .stTextInput input {
            background-color: #0f172a !important;
            color: white !important;
            border: 1px solid #334155 !important;
            border-radius: 12px !important;
            padding: 14px !important;
        }

        .stButton button {
            width: 100%;
            background: linear-gradient(
                90deg,
                #4f46e5,
                #7c3aed
            );
            color: white;
            border: none;
            padding: 14px;
            border-radius: 12px;
            font-size: 16px;
            font-weight: 600;
        }

        .google-btn button {
            background: white !important;
            color: black !important;
            border-radius: 12px !important;
            border: none !important;
        }

        h1, h2, h3, h4, h5, h6,
        p, span, label {
            color: white !important;
        }

        </style>
        """, unsafe_allow_html=True)

    else:

        st.markdown("""
        <style>

        .stApp {
            background: #f8fafc;
            color: black;
        }

        section[data-testid="stSidebar"] {
            background: white;
            border-right: 1px solid #ddd;
        }

        .main-title {
            text-align: center;
            font-size: 52px;
            font-weight: 700;
            color: #0f172a;
            margin-bottom: 10px;
        }

        .sub-title {
            text-align: center;
            color: #475569;
            margin-bottom: 40px;
            font-size: 18px;
        }

        .auth-box {
            background: white;
            padding: 40px;
            border-radius: 22px;
            max-width: 520px;
            margin: auto;
            margin-top: 30px;
            border: 1px solid #ddd;
            box-shadow: 0 8px 25px rgba(0,0,0,0.08);
        }

        .stTextInput input {
            background-color: white !important;
            color: black !important;
            border: 1px solid #ccc !important;
            border-radius: 12px !important;
            padding: 14px !important;
        }

        .stButton button {
            width: 100%;
            background: linear-gradient(
                90deg,
                #4f46e5,
                #7c3aed
            );
            color: white;
            border: none;
            padding: 14px;
            border-radius: 12px;
            font-size: 16px;
            font-weight: 600;
        }

        h1, h2, h3, h4, h5, h6,
        p, span, label {
            color: black !important;
        }

        </style>
        """, unsafe_allow_html=True)