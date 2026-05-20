from database.connection import get_connection


def create_chat(user_id, title):
    conn = get_connection()
    cursor = conn.cursor()

    query = "INSERT INTO chats(user_id,title) VALUES(%s,%s)"
    cursor.execute(query, (user_id, title))

    conn.commit()

    return cursor.lastrowid

def delete_chat(chat_id):
    conn = get_connection()
    cursor = conn.cursor()

    # 1. Delete all messages linked to this chat
    cursor.execute(
        "DELETE FROM messages WHERE chat_id = %s",
        (chat_id,)
    )

    # 2. Delete chat from chats table (IMPORTANT: column is "id")
    cursor.execute(
        "DELETE FROM chats WHERE id = %s",
        (chat_id,)
    )

    conn.commit()
    conn.close()
    
def get_user_chats(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM chats WHERE user_id=%s ORDER BY id DESC"
    cursor.execute(query, (user_id,))

    return cursor.fetchall()