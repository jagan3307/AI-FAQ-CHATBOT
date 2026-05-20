# 🤖 AI FAQ Chatbot

An AI-powered FAQ chatbot built using **Streamlit**, **MySQL**, and **Groq LLM** that can:

- 💬 Answer FAQ questions
- 📄 Read PDF documents and answer based on content
- 💡 Generate FAQs from business ideas
- 🔐 User Authentication (Login / Signup)
- 🕘 Save chat history
- 🌙 Dark & Light Mode Support

---

# 🚀 Features

## ✅ AI Chatbot
- Ask questions naturally
- AI-generated responses using Groq LLM
- ChatGPT-style interface

## ✅ FAQ System
Supports:
- College FAQs
- HR FAQs
- Customer Support FAQs
- Product Assistance FAQs

---

## ✅ PDF Knowledge Base
Upload:
- Company documents
- College handbooks
- HR policies
- Product manuals

The chatbot reads the PDF and answers questions based on uploaded content.

---

## ✅ Business Idea → FAQ Generator
Enter your:
- Startup idea
- Business concept
- College idea

The AI automatically generates FAQs and answers.

---

## ✅ Authentication System
- User Signup
- User Login
- Logout Functionality

Passwords are securely stored using hashing.

---

## ✅ Chat History
- Saves all conversations
- Sidebar chat history
- Open previous chats anytime
- Delete chats option

---

## ✅ Theme Support
- 🌞 Light Mode
- 🌙 Dark Mode

---

# 🛠️ Tech Stack

| Technology | Usage |
|------------|------|
| Python | Backend Logic |
| Streamlit | Frontend UI |
| MySQL | Database |
| Groq API | AI Responses |
| PyPDF | PDF Text Extraction |
| bcrypt | Password Hashing |

---

# 📂 Project Structure

```bash
AI_FAQ_CHATBOT/
│
├── app.py
│
├── auth/
│   ├── login.py
│   ├── signup.py
│   └── logout.py
│
├── chatbot/
│   ├── ai_engine.py
│   ├── response_handler.py
│   ├── faq_data.py
│   ├── faq_generator.py
│   ├── dynamic_faq.py
│   ├── pdf_loader.py
│   └── context.py
│
├── database/
│   ├── connection.py
│   ├── init_db.py
│   ├── chat_db.py
│   └── message_db.py
│
├── ui/
│   ├── sidebar.py
│   ├── chat_ui.py
│   └── styles.py
│
├── utils/
│   └── session.py
│
├── .env
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/AI_FAQ_CHATBOT.git
cd AI_FAQ_CHATBOT
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

### Windows
```bash
venv\Scripts\activate
```

### Mac/Linux
```bash
source venv/bin/activate
```

---

## 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

---

# 🗄️ MySQL Database Setup

## Create Database

```sql
CREATE DATABASE ai_faq_chatbot;
```

---

## Configure `.env`

Create `.env` file:

```env
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DATABASE=ai_faq_chatbot

GROQ_API_KEY=your_groq_api_key
```

---

## Initialize Database

```bash
python -m database.init_db
```

---

# ▶️ Run Application

```bash
streamlit run app.py
```

---

# 📸 Sample Use Cases

## 🎓 College FAQs
- Admission process
- Fees structure
- Hostel details
- Placement support

## 🏢 HR Support
- Leave policy
- Salary information
- Work from home policy

## 🛒 Product Assistance
- Setup instructions
- Features
- Troubleshooting

---

# 🧠 AI Workflow

```text
User Question
      ↓
Response Handler
      ↓
Check Static FAQs
      ↓
Check Dynamic FAQs
      ↓
Check PDF Context
      ↓
AI Model (Groq)
      ↓
Return Response
```

---

# 🔥 Future Improvements

- Voice Assistant
- Multi-language Support
- Admin Dashboard
- Vector Database
- RAG-based Search
- Deployment on AWS/Render

---

# 👨‍💻 Author

Developed by **Jagan G**

---

# 📜 License

This project is for educational and learning purposes.
