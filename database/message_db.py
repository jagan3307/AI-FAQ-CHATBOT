from database.connection import get_connection


def save_message(chat_id, role, content):
    conn = get_connection()
    cursor = conn.cursor()

    query = "INSERT INTO messages(chat_id,role,content) VALUES(%s,%s,%s)"
    cursor.execute(query, (chat_id, role, content))

    conn.commit()


def get_messages(chat_id):
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT role,content FROM messages WHERE chat_id=%s"
    cursor.execute(query, (chat_id,))

    return cursor.fetchall()