import streamlit as st
from database.chat_db import get_user_chats
from database.message_db import get_messages


def sidebar(user_id):

    with st.sidebar:

        st.title("💬 Chat History")

        if st.button("➕ New Chat"):
            st.session_state.chat_id = None
            st.session_state.messages = []
            st.rerun()

        chats = get_user_chats(user_id)

        for chat in chats:

            chat_id = chat[0]
            title = chat[2]

            col1, col2 = st.columns([4, 1])

            with col1:
                if st.button(title, key=f"open_{chat_id}"):

                    st.session_state.chat_id = chat_id

                    old_messages = get_messages(chat_id)

                    st.session_state.messages = []

                    for role, content in old_messages:
                        st.session_state.messages.append({
                            "role": role,
                            "content": content
                        })

                    st.rerun()

            with col2:
                if st.button("🗑️", key=f"del_{chat_id}"):

                    from database.chat_db import delete_chat

                    delete_chat(chat_id)

                    if st.session_state.chat_id == chat_id:
                        st.session_state.chat_id = None
                        st.session_state.messages = []

                    st.rerun()