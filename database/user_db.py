import bcrypt
from database.connection import get_connection


def register_user(username, email, password):
    conn = get_connection()
    cursor = conn.cursor()

    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    try:
        query = "INSERT INTO users(username,email,password) VALUES(%s,%s,%s)"
        cursor.execute(query, (username, email, hashed))
        conn.commit()
        return True
    except:
        return False


def login_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE username=%s"
    cursor.execute(query, (username,))

    user = cursor.fetchone()

    if user:
        stored_password = user[3].encode() if isinstance(user[3], str) else user[3]

        if bcrypt.checkpw(password.encode(), stored_password):
            return user

    return None