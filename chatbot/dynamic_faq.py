import re

def parse_faqs(text):

    qa_pairs = []

    questions = re.findall(r"Q\d+:\s*(.*)", text)
    answers = re.findall(r"A\d+:\s*(.*)", text)

    for q, a in zip(questions, answers):
        qa_pairs.append({
            "question": q.lower(),
            "answer": a
        })

    return qa_pairs


def match_faq(user_input, faq_list):

    user_input = user_input.lower()

    for faq in faq_list:
        if faq["question"] in user_input:
            return faq["answer"]

    return None