from database.connection import supabase


def save_message(chat_id, role, content):

    supabase.table("messages").insert({
        "chat_id": chat_id,
        "role": role,
        "content": content
    }).execute()


def get_messages(chat_id):

    response = supabase.table("messages") \
        .select("*") \
        .eq("chat_id", chat_id) \
        .order("created_at") \
        .execute()

    messages = []

    for msg in response.data:

        messages.append((
            msg["role"],
            msg["content"]
        ))

    return messages