import streamlit as st
import google.generativeai as genai

# ✅ Load your Gemini API key from Streamlit secrets
GOOGLE_API_KEY = st.secrets.get("GOOGLE_API_KEY")

# ✅ Configure Gemini API
genai.configure(api_key=GOOGLE_API_KEY)

# ✅ Create the model using the correct name
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro")  # <-- This is the correct model name

# ✅ Streamlit UI
st.set_page_config(page_title="Gemini AI Assistant", page_icon="🤖")
st.title("🤖 Gemini-Powered AI Assistant")
st.markdown("Ask anything and get a smart response powered by Google's Gemini AI!")

# ✅ Text input
user_prompt = st.text_area("Enter your prompt:", placeholder="e.g. Give me 5 YouTube video ideas")

if st.button("Ask Gemini"):
    if not user_prompt.strip():
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Thinking..."):
            try:
                response = model.generate_content(user_prompt)
                st.subheader("📌 Gemini's Response")
                st.write(response.text)
            except Exception as e:
                st.error(f"❌ Gemini API Error:\n\n{str(e)}")
