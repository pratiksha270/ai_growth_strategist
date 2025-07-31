import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="🤖 AI Assistant", layout="centered")
st.title("🤖 Gemini-Powered AI Assistant")
st.write("Ask anything and get a smart response powered by AI!")

# Set API key
client = OpenAI(api_key=st.secrets["GOOGLE_API_KEY"])  # make sure your secret key is set

# Input prompt
prompt = st.text_input("Enter your prompt:", placeholder="e.g., give me 5 YouTube ideas")

if st.button("💡 Get Response") and prompt.strip():
    with st.spinner("Thinking..."):
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            st.success("AI Response:")
            st.write(response.choices[0].message.content)
        except Exception as e:
            st.error(f"❌ Error: {e}")
