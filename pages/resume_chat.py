import streamlit as st
import requests

st.title("💼 Resume Chat")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

uploaded_file = st.file_uploader("Upload Resume (PDF or DOC)", type=["pdf", "doc", "docx"])
question = st.chat_input("Ask about this resume")

if question:
    if uploaded_file is None:
        st.error("Please upload a resume first.")
    else:
        files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
        payload = {"question": question}

        # n8n webhook
        response = requests.post(
            "https://sachintendulkar.app.n8n.cloud/webhook/fd3ac7d5-612c-4bb8-86b6-dbbde3d0223c",
            data=payload, files=files
        )

        answer = response.text
        st.session_state["messages"].append(("user", question))
        st.session_state["messages"].append(("assistant", answer))

# Display chat history
for role, msg in st.session_state["messages"]:
    st.chat_message(role).write(msg)
