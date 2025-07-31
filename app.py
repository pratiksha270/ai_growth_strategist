import streamlit as st
import requests
import json

st.set_page_config(page_title="🤗 Hugging Face AI Assistant")
st.title("🤗 Hugging Face AI Assistant")
st.markdown("""
Ask anything and get a smart response using open-source models from Hugging Face!
""")

# Input section
model_name = st.selectbox("Choose a model:", [
    "HuggingFaceH4/zephyr-7b-beta",
    "mistralai/Mistral-7B-Instruct-v0.1"
])

prompt = st.text_input("Enter your prompt:", placeholder="e.g. Tell me about AI")

# Load Hugging Face API key from secrets
api_key = st.secrets["HUGGINGFACE_API_KEY"]

# Send query to Hugging Face Inference API
def query_huggingface(prompt_text):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "inputs": prompt_text,
        "parameters": {"max_new_tokens": 300, "temperature": 0.7}
    }
    url = f"https://api-inference.huggingface.co/models/{model_name}"
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        output = response.json()
        try:
            return output[0]["generated_text"]
        except:
            return json.dumps(output)
    else:
        return f"❌ Hugging Face API Error {response.status_code}: {response.reason}\n{response.text}"

# Run on button click
if st.button("Ask AI") and prompt:
    with st.spinner("Thinking..."):
        result = query_huggingface(prompt)
        st.markdown("---")
        st.subheader("🧠 AI Response:")
        st.write(result)
