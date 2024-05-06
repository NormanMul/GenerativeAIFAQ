# streamlit_app.py
import streamlit as st
import requests
from uuid import uuid4

# API URL
API_URL = "http://0.0.0.0:8004/national_id_application/query"

# Function to query the API
def national_id_application_query(content: str, session_id: str) -> dict:
    response = requests.post(
        API_URL, json={"content": content, "session_id": session_id}
    )
    data = response.json()
    return {
        "thinking": data.get("thinking", ""),
        "intent": data.get("intent", ""),
        "response": data.get("response", ""),
    }

# Initialize the conversation history
if "history" not in st.session_state:
    st.session_state["history"] = []

# Streamlit App UI
def main():
    st.title("🦜 Northstar: Chat and Ask your ID Application")
    st.title("Made by DoaIbu")

    query = st.text_input("## How can I help you? Enter your query regarding the National ID application:")

    if st.button("Submit"):
        session_id = str(uuid4())
        response = national_id_application_query(query, session_id)
        st.session_state["history"].append({"role": "user", "content": query})
        st.session_state["history"].append({"role": "bot", "content": response["response"]})

    st.markdown("---")
    st.markdown("### Conversation History")

    for message in st.session_state["history"]:
        if message["role"] == "user":
            st.write(f"🧑‍💻 **You:** {message['content']}")
        else:
            st.write(f"🤖 **Starpeeps:** {message['content']}")

if __name__ == "__main__":
    main()
