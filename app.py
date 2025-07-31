import streamlit as st
import requests
import json

# Hugging Face API details
API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
headers = {
    "Authorization": f"Bearer {st.secrets['HUGGINGFACE_API_KEY']}"
}

# Streamlit UI
st.set_page_config(page_title="🤖 Hugging Face Assistant")
st.title("🤖 Gemini-like Assistant (via Hugging Face)")

st.markdown("Ask anything and get a smart response powered by Hugging Face Zephyr model!")

user_input = st.text_area("Enter your prompt:", placeholder="e.g. Give me 5 YouTube video ideas")

if st.button("Ask AI"):
    if not user_input.strip():
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("💬 Generating response..."):
            payload = {
                "inputs": user_input,
                "parameters": {
                    "max_new_tokens": 300,
                    "return_full_text": False
                }
            }
            response = requests.post(API_URL, headers=headers, json=payload)

            if response.status_code == 200:
                output = response.json()
                try:
                    st.success(output[0]["generated_text"])
                except Exception:
                    st.error("❌ Could not parse response. Try again.")
            else:
                st.error(f"❌ Hugging Face API Error {response.status_code}: {response.text}")
