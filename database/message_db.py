from database.connection import supabase


def save_message(chat_id, role, content):

    data = {
        "chat_id": chat_id,
        "role": role,
        "content": content
    }

    supabase.table(
        "messages"
    ).insert(data).execute()


def get_messages(chat_id):

    response = supabase.table(
        "messages"
    ).select("*") \
    .eq("chat_id", chat_id) \
    .order("id") \
    .execute()

    messages = []

    for msg in response.data:

        messages.append(
            (
                msg["role"],
                msg["content"]
            )
        )

    return messages