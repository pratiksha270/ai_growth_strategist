import streamlit as st
import requests
import os

st.set_page_config(page_title="Hugging Face AI Assistant", layout="centered")
st.title("🤗 Hugging Face AI Assistant")
st.write("Ask anything and get a smart response using open-source models from Hugging Face!")

# Choose from working models
model_name = st.selectbox("Choose a model:", [
    "google/flan-t5-large",
    "tiiuae/falcon-7b-instruct",
    "facebook/opt-1.3b",
    "bigcode/starcoder"
])

prompt = st.text_input("Enter your prompt:")

if st.button("Ask AI") and prompt:
    API_URL = f"https://api-inference.huggingface.co/models/{model_name}"
    headers = {"Authorization": f"Bearer {st.secrets['HUGGINGFACE_API_KEY']}"}

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 100,
            "temperature": 0.7
        }
    }

    with st.spinner("Thinking..."):
        response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        try:
            generated_text = response.json()[0]["generated_text"]
            st.success(generated_text)
        except Exception as e:
            st.error(f"Unexpected format: {e}")
            st.json(response.json())
    else:
        st.error(f"Hugging Face API Error {response.status_code}: {response.text}")
