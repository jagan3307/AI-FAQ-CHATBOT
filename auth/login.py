import streamlit as st
from database.connection import supabase


def login_page():

    # ==========================================
    # CUSTOM CSS
    # ==========================================
    st.markdown("""
    <style>

    /* HIDE SIDEBAR */
    section[data-testid="stSidebar"] {
        display: none;
    }

    .stApp {
        background-color: #f3f4f8;
    }

    .block-container {
        padding-top: 2rem;
    }

    /* LOGIN CARD */
    .login-card {
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

    /* SUBTITLE */
    .subtitle {
        text-align: center;
        color: #7b7b7b;
        font-size: 20px;
        margin-bottom: 35px;
    }

    /* INPUTS */
    .stTextInput > div > div > input {
        height: 60px;
        border-radius: 18px;
        border: 1px solid #dcdcdc;
        padding-left: 20px;
        font-size: 18px;
        background-color: #fafafa;
    }

    /* LOGIN BUTTON */
    .stButton > button {
        width: 100%;
        height: 60px;
        border-radius: 18px;
        border: none;
        background: linear-gradient(90deg,#5b5cf0,#6c63ff);
        color: white;
        font-size: 22px;
        font-weight: 600;
        margin-top: 15px;
    }

    .stButton > button:hover {
        background: linear-gradient(90deg,#4c4df0,#5f56ff);
        color: white;
    }

    /* GOOGLE BUTTON */
    div[data-testid="stButton"] button[kind="secondary"] {
        background: white !important;
        color: black !important;
        border: 1px solid #dadce0 !important;
    }

    /* REGISTER */
    .register {
        text-align: center;
        margin-top: 30px;
        font-size: 18px;
    }

    .register span {
        color: #5b5cf0;
        font-weight: 600;
    }

    </style>
    """, unsafe_allow_html=True)

    # ==========================================
    # LOGIN CARD START
    # ==========================================
    st.markdown("""
    <div class="login-card">

    <div class="title">
    Welcome Back
    </div>

    <div class="subtitle">
    Login to continue
    </div>
    """, unsafe_allow_html=True)

    # ==========================================
    # EMAIL INPUT
    # ==========================================
    email = st.text_input(
        "Email Address",
        placeholder="Enter your email"
    )

    # ==========================================
    # PASSWORD INPUT
    # ==========================================
    password = st.text_input(
        "Password",
        type="password",
        placeholder="Enter your password"
    )

    # ==========================================
    # SHOW PASSWORD
    # ==========================================
    show_password = st.checkbox("Show Password")

    if show_password:
        st.info(f"Password: {password}")

    # ==========================================
    # LOGIN BUTTON
    # ==========================================
    if st.button("Login"):

        if not email or not password:

            st.warning("Please enter email and password")

        else:

            try:

                response = supabase.auth.sign_in_with_password(
                    {
                        "email": email,
                        "password": password
                    }
                )

                user = response.user

                if user:

                    st.session_state.logged_in = True

                    st.session_state.user = (
                        user.id,
                        user.email
                    )

                    st.success("Login Successful ✅")

                    st.rerun()

            except Exception as e:

                st.error("Invalid Email or Password")
                st.exception(e)

    # ==========================================
    # DIVIDER
    # ==========================================
    st.markdown("""
    <div style='text-align:center;
                margin-top:25px;
                margin-bottom:10px;
                color:gray;
                font-size:18px;'>
        OR
    </div>
    """, unsafe_allow_html=True)

    # ==========================================
    # GOOGLE LOGIN BUTTON
    # ==========================================
    google_login = st.button(
        "🔵 Continue with Google",
        use_container_width=True,
        type="secondary"
    )

    if google_login:

        try:

            response = supabase.auth.sign_in_with_oauth(
                {
                    "provider": "google",
                    "options": {
                        "redirect_to":
                        "http://localhost:8501"
                    }
                }
            )

            st.link_button(
                "👉 Click Here to Login with Google",
                response.url,
                use_container_width=True
            )

        except Exception as e:

            st.error("Google Login Failed")
            st.exception(e)

    # ==========================================
    # REGISTER TEXT
    # ==========================================
    st.markdown("""
    <div class="register">
    Don't have an account?
    <span>Register</span>
    </div>

    </div>
    """, unsafe_allow_html=True)