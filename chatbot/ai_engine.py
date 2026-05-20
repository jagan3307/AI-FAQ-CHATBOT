from groq import Groq
from config.settings import GROQ_API_KEY
from chatbot.prompts import system_prompt

client = Groq(api_key=GROQ_API_KEY)

def generate_response(messages, context=""):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": system_prompt + f"""

You must also use this PDF context to answer:
{context}
"""
            },
            *messages
        ]
    )

    return response.choices[0].message.content