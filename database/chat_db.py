from database.connection import supabase


def create_chat(user_id, title):

    data = {
        "user_id": str(user_id),
        "title": title
    }

    response = supabase.table(
        "chats"
    ).insert(data).execute()

    return response.data[0]["id"]


def get_user_chats(user_id):

    response = supabase.table(
        "chats"
    ).select("*") \
    .eq("user_id", str(user_id)) \
    .order("id", desc=True) \
    .execute()

    return response.data


def delete_chat(chat_id):

    supabase.table(
        "messages"
    ).delete() \
    .eq("chat_id", chat_id) \
    .execute()

    supabase.table(
        "chats"
    ).delete() \
    .eq("id", chat_id) \
    .execute()