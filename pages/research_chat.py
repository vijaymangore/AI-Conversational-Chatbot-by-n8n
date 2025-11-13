import streamlit as st
import requests

st.title("📚 Research Chat")

if "research_messages" not in st.session_state:
    st.session_state["research_messages"] = []

uploaded_file = st.file_uploader("Upload Research Paper or Data (PDF, CSV, DOC)", type=["pdf", "csv", "doc"])
question = st.chat_input("Ask about this research paper or dataset")

if question:
    if uploaded_file is None:
        st.error("Please upload a research file first.")
    else:
        files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
        payload = {"question": question}

        response = requests.post(
            "https://sachintendulkar.app.n8n.cloud/webhook/298078b1-5ec3-4a35-811e-9e7063e5358e",
            data=payload, files=files
        )

        answer = response.text
        st.session_state["research_messages"].append(("user", question))
        st.session_state["research_messages"].append(("assistant", answer))

# Display chat history
for role, msg in st.session_state["research_messages"]:
    st.chat_message(role).write(msg)
