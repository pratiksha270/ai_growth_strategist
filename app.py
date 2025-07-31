import streamlit as st
import requests
import json

# TITLE
st.set_page_config(page_title="🧠 AI Business Growth Strategist")
st.title("🚀 AI Business Growth Strategist & Problem Solver")
st.markdown("Diagnose business challenges and generate tailored strategies with an open-source AI model via Hugging Face!")

# Hugging Face API config
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
HF_TOKEN = st.secrets["HUGGINGFACE_API_KEY"]

headers = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json"
}

# Form Input
with st.form("business_form"):
    st.subheader("📝 Step 1: Business Information")
    name = st.text_input("Business Name")
    industry = st.text_input("Industry")
    audience = st.text_input("Target Audience")
    goal = st.text_input("Business Goal")
    problem = st.text_area("Describe the Current Problem")

    submit = st.form_submit_button("📨 Diagnose Problem")

# Prompt builder
def build_prompt(name, industry, audience, goal, problem):
    return f"""
You are an expert business strategist AI.

A business named **{name}** in the **{industry}** industry is targeting **{audience}**.
Their primary goal is to **{goal}**.
They are currently facing the following problem: "{problem}"

Please:
1. Analyze the possible causes
2. Suggest a high-level action plan
3. Recommend marketing or sales strategies
4. Give any tools or trends they should explore
Respond in simple, business-friendly language.
"""

# API caller
def query_huggingface(prompt):
    payload = {
        "inputs": prompt,
        "parameters": {
            "temperature": 0.7,
            "max_new_tokens": 400
        }
    }

    response = requests.post(API_URL, headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        return response.json()[0]["generated_text"]
    else:
        st.error(f"❌ Hugging Face API Error {response.status_code}: {response.text}")
        return None

# Handle submission
if submit:
    if all([name, industry, audience, goal, problem]):
        with st.spinner("🔍 Sending to Hugging Face model..."):
            prompt = build_prompt(name, industry, audience, goal, problem)
            output = query_huggingface(prompt)
            if output:
                st.subheader("📊 AI-Powered Business Strategy")
                st.write(output)
    else:
        st.warning("⚠️ Please fill out all fields before submitting.")
