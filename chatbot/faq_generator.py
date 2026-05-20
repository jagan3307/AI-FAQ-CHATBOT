from groq import Groq
from config.settings import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

def generate_faqs_from_idea(idea):

    prompt = f"""
You are an expert FAQ generator.

Generate 10 high-quality FAQs and answers for this idea:

IDEA:
{idea}

FORMAT STRICTLY:
Q1: ...
A1: ...
Q2: ...
A2: ...
...
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content