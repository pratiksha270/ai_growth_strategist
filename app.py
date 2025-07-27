import streamlit as st
import google.generativeai as genai
import os

# Load Gemini API key from Streamlit Secrets
GOOGLE_API_KEY = st.secrets.get("GOOGLE_API_KEY")

# Configure Gemini
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the model
model = genai.GenerativeModel('gemini-pro')

# Streamlit App UI
st.set_page_config(page_title="Gemini AI Assistant", page_icon="🤖")
st.title("🤖 Gemini-Powered AI Assistant")
st.markdown("Ask anything and get a smart response powered by Google's Gemini AI!")

# Prompt input
user_prompt = st.text_area("Enter your prompt:", placeholder="e.g. Give me 5 ideas for a YouTube video")

if st.button("Ask Gemini"):
    if user_prompt.strip() == "":
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Sending prompt to Gemini..."):
            try:
                response = model.generate_content(user_prompt)
                st.subheader("📌 Gemini's Response")
                st.write(response.text)
            except Exception as e:
                st.error(f"❌ Gemini API Error:\n\n{str(e)}")
