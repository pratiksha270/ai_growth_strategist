import streamlit as st
import openai
import os

# App title
st.set_page_config(page_title="AI Assistant (OpenAI)", layout="centered")
st.title("🤖 OpenAI-Powered AI Assistant")
st.markdown("Ask anything and get a smart response powered by OpenAI GPT!")

# API key from secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# User input
user_prompt = st.text_area("Enter your prompt:", height=150)

if st.button("Generate Response"):
    if not user_prompt.strip():
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("💬 Thinking..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": user_prompt}]
                )
                reply = response.choices[0].message.content.strip()
                st.success("✅ Response:")
                st.write(reply)

            except Exception as e:
                st.error(f"❌ OpenAI API Error:\n\n{str(e)}")
