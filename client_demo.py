# client_demo.py

import requests
from typing import Dict
from uuid import uuid4

def national_id_application_query(url: str, content: str, session_id: str) -> Dict:
    response = requests.post(
        url, json={"content": content, "session_id": session_id}
    )
    data = response.json()
    return {
        "thinking": data.get("thinking", ""),
        "intent": data.get("intent", ""),
        "response": data.get("response", ""),
    }

if __name__ == "__main__":
    test_url = "http://0.0.0.0:8004/national_id_application/query"
    content = "Where is the Citizen Services Department?"
    session_id = str(uuid4())
    print(f"Current session_id: {session_id}")
    resp = national_id_application_query(test_url, content, session_id)
    print(resp)
