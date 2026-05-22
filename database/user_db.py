from database.connection import supabase
import bcrypt


def register_user(username, email, password):

    hashed = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    ).decode()

    data = {
        "username": username,
        "email": email,
        "password": hashed
    }

    response = supabase.table("users").insert(data).execute()

    return response


def login_user(username, password):

    response = supabase.table("users") \
        .select("*") \
        .eq("username", username) \
        .execute()

    users = response.data

    if len(users) == 0:
        return None

    user = users[0]

    if bcrypt.checkpw(
        password.encode(),
        user["password"].encode()
    ):
        return (
            user["id"],
            user["username"]
        )

    return None