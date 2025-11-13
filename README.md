🧠 AI Conversational Chatbot — n8n + Streamlit Integration
📌 Overview
This project is an AI-powered Conversational Chatbot that analyzes uploaded documents such as resumes and research papers.
It integrates Streamlit for the user interface and n8n for backend automation using Google Gemini (PaLM) to extract, process, and answer questions directly from the uploaded documents.

🚀 Features

🧾 Upload and analyze PDF, DOCX, or CSV files

💬 Ask natural language questions about the content

🤖 Uses n8n workflow with Google Gemini AI for intelligent responses

💡 Answers strictly from the uploaded document — no hallucinations

🧠 Maintains short-term context using Memory Buffer in n8n

🧩 Project Structure
project/
│
├── app.py                         # Main Streamlit app (home page)
│
├── requirements.txt                # Python dependencies
│
└── pages/
    ├── resume_chat.py             # Resume Q&A interface
    └── research_chat.py           # Research/CSV Q&A interface

⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/vijaymangore/AI-CONVERSATIONAL-CHATBOT.git
cd AI-CONVERSATIONAL-CHATBOT

2️⃣ Create and Activate Virtual Environment
python -m venv venv
venv\Scripts\activate     # On Windows
# or
source venv/bin/activate  # On Mac/Linux

3️⃣ Install Dependencies
pip install -r requirements.txt


requirements.txt

streamlit
requests

4️⃣ Run the Streamlit App
streamlit run app.py


Now open the app in your browser at:
👉 http://localhost:8501

🧠 How It Works
Frontend (Streamlit)

Users upload a file (Resume or Research Paper).

They input a question via chat.

The app sends both file and question to a Webhook URL hosted on n8n.

Backend (n8n Workflow)

Workflow Summary:

Webhook Node: Receives uploaded file and question.

Extract from File: Extracts text from the uploaded file (PDF/DOC).

Google Gemini Chat Model: Uses Gemini to process language.

AI Agent: Answers question strictly from the document text.

Respond to Webhook: Sends the AI-generated answer back to Streamlit.

Workflow Webhooks:

Resume Chat Webhook →
https://sachintendulkar.app.n8n.cloud/webhook-test/298078b1-5ec3-4a35-811e-9e7063e5358e

Research Chat Webhook →
https://sachintendulkar.app.n8n.cloud/webhook-test/fd3ac7d5-612c-4bb8-86b6-dbbde3d0223c

🧩 Files Description
app.py

Displays the project home page and navigation between pages.

pages/resume_chat.py

Handles document upload (resumes), connects to Resume n8n Webhook, and displays conversation.

pages/research_chat.py

Handles upload of research papers or datasets, connects to Research Webhook, and displays conversation.

🧪 Example Usage

Open the app.

Navigate to “Resume Chat 💼”.

Upload a resume.pdf.

Ask: “What is the candidate’s total experience?”

Receive an AI-generated answer — extracted only from the uploaded file.

🛠️ Tech Stack
Layer	Technology
Frontend	Streamlit
Backend Automation	n8n
LLM	Google Gemini (PaLM)
Memory	LangChain Buffer Window
File Parsing	n8n Extract from File Node
Deployment	Streamlit Cloud + n8n Cloud
📤 Deployment
Streamlit Cloud

Push your project to GitHub.

Go to https://share.streamlit.io

Select your repo → main branch → app.py

Deploy 🚀

n8n Cloud

Your workflow (final project.json) can be imported directly to n8n:

Open your n8n workspace → Import from file

Select final project.json

Activate the workflow.

🙏 Credits

Developed by Vijaykumar Mangore

📧 Email: vkmangore@gmail.com



