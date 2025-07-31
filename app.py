import streamlit as st
import requests

# Hugging Face API token from secrets
api_token = st.secrets["HUGGINGFACE_API_KEY"]

# Model options
MODEL_OPTIONS = {
    "Mistral-7B Instruct": "mistralai/Mistral-7B-Instruct-v0.1",
    "Falcon-7B Instruct": "tiiuae/falcon-7b-instruct"
}

# Title and description
st.title("🤖 Hugging Face AI Assistant")
st.markdown("Ask anything and get a smart response using open-source models from Hugging Face!")

# Model selection dropdown
model_label = st.selectbox("Choose a model:", list(MODEL_OPTIONS.keys()))
model_name = MODEL_OPTIONS[model_label]
API_URL = f"https://api-inference.huggingface.co/models/{model_name}"

# Prompt input
prompt = st.text_input("Enter your prompt:", placeholder="e.g. Give me 5 YouTube content ideas")

# Button to trigger inference
if st.button("Ask AI") and prompt:
    headers = {"Authorization": f"Bearer {api_token}"}
    payload = {"inputs": prompt}

    with st.spinner("Generating response..."):
        response = requests.post(API_URL, headers=headers, json=payload)

    # Handle error
    if response.status_code == 200:
        output = response.json()
        if isinstance(output, list):
            st.success(output[0]['generated_text'])
        else:
            st.warning("Unexpected response format. Try another prompt.")
    else:
        st.error(f"Hugging Face API Error {response.status_code}: {response.text}")
