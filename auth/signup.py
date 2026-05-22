import streamlit as st
from database.user_db import register_user


def signup_page():

    # ==========================================
    # CUSTOM CSS
    # ==========================================
    st.markdown("""
    <style>

    /* HIDE SIDEBAR */
    section[data-testid="stSidebar"] {
        display: none;
    }

    /* MAIN BACKGROUND */
    .stApp {
        background-color: #f3f4f8;
    }

    /* REMOVE DEFAULT PADDING */
    .block-container {
        padding-top: 2rem;
    }

    /* SIGNUP CARD */
    .signup-card {
        background: white;
        padding: 45px;
        border-radius: 28px;
        max-width: 520px;
        margin: auto;
        margin-top: 30px;
        box-shadow: 0 4px 30px rgba(0,0,0,0.05);
    }

    /* TITLE */
    .title {
        text-align: center;
        font-size: 52px;
        font-weight: 700;
        color: black;
        margin-bottom: 10px;
    }

    .subtitle {
        text-align: center;
        color: #7b7b7b;
        font-size: 20px;
        margin-bottom: 35px;
    }

    /* INPUT BOX */
    .stTextInput > div > div > input {
        height: 60px;
        border-radius: 18px;
        border: 1px solid #dcdcdc;
        padding-left: 20px;
        font-size: 18px;
        background-color: #fafafa;
    }

    /* BUTTON */
    .stButton > button {
        width: 100%;
        height: 60px;
        border-radius: 18px;
        border: none;
        background: linear-gradient(90deg,#5b5cf0,#6c63ff);
        color: white;
        font-size: 24px;
        font-weight: 600;
        margin-top: 15px;
    }

    .stButton > button:hover {
        background: linear-gradient(90deg,#4c4df0,#5f56ff);
        color: white;
    }

    /* LOGIN TEXT */
    .login {
        text-align: center;
        margin-top: 30px;
        font-size: 18px;
    }

    .login span {
        color: #5b5cf0;
        font-weight: 600;
    }

    </style>
    """, unsafe_allow_html=True)

    # ==========================================
    # CARD START
    # ==========================================
    st.markdown("""
    <div class="signup-card">

    <div class="title">
    Create Account
    </div>

    <div class="subtitle">
    Register to continue
    </div>
    """, unsafe_allow_html=True)

    # ==========================================
    # INPUTS
    # ==========================================
    username = st.text_input(
        "Username",
        placeholder="Enter username"
    )

    email = st.text_input(
        "Email Address",
        placeholder="Enter your email"
    )

    password = st.text_input(
        "Password",
        type="password",
        placeholder="Enter your password"
    )

    # ==========================================
    # REGISTER BUTTON
    # ==========================================
    if st.button("Register"):

        if not username or not email or not password:

            st.warning("Please fill all fields")

        else:

            try:

                user = register_user(
                    email,
                    password
                )

                if user:

                    st.success(
                        "Account Created Successfully ✅"
                    )

                else:

                    st.error(
                        "Signup Failed"
                    )

            except Exception as e:

                st.error("Signup Failed")
                st.exception(e)

    # ==========================================
    # LOGIN TEXT
    # ==========================================
    st.markdown("""
    <div class="login">
    Already have an account?
    <span>Login</span>
    </div>

    </div>
    """, unsafe_allow_html=True)