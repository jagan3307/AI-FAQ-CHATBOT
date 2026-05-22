from database.connection import supabase


def create_chat(user_id, title):

    response = supabase.table("chats").insert({
        "user_id": user_id,
        "title": title
    }).execute()

    return response.data[0]["id"]


def get_user_chats(user_id):

    response = supabase.table("chats") \
        .select("*") \
        .eq("user_id", user_id) \
        .order("created_at", desc=True) \
        .execute()

    chats = []

    for chat in response.data:

        chats.append((
            chat["id"],
            chat["user_id"],
            chat["title"]
        ))

    return chats


def delete_chat(chat_id):

    supabase.table("messages") \
        .delete() \
        .eq("chat_id", chat_id) \
        .execute()

    supabase.table("chats") \
        .delete() \
        .eq("id", chat_id) \
        .execute()