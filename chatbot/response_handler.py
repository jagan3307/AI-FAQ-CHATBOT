from chatbot.faq_data import faq_data
from chatbot.ai_engine import generate_response
from chatbot.context import get_pdf_context
from chatbot.dynamic_faq import match_faq
import streamlit as st


def get_bot_response(prompt, messages):

    lower_prompt = prompt.lower()

    if "what can you do" in lower_prompt or "who are you" in lower_prompt:
        return """
I am an AI FAQ Assistant 🤖

I can help you with:

✔ College FAQs (admission, fees, exams)  
✔ HR FAQs (leave policy, salary, attendance)  
✔ Customer Support FAQs (orders, refunds, complaints)  
✔ Product Assistance FAQs (features, setup, troubleshooting)  

I can also:
📄 Read PDF documents and answer questions  
💡 Generate FAQs from your business or idea  
💬 Act like a smart support assistant for any domain  
"""

    if lower_prompt in faq_data:
        return faq_data[lower_prompt]

    dynamic_faqs = st.session_state.get("dynamic_faqs", [])

    match = match_faq(lower_prompt, dynamic_faqs)

    if match:
        return match

    pdf_context = st.session_state.get("pdf_context", "")

    return generate_response(messages, pdf_context)