import streamlit as st
import google.generativeai as genai
import json

# Load credentials from Streamlit Secrets
genai.configure(credentials=json.loads(st.secrets["GOOGLE_SERVICE_ACCOUNT_JSON"]))

# Set Streamlit page config
st.set_page_config(
    page_title="AI Business Growth Strategist",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Title
st.title("🚀 AI Business Growth Strategist & Problem Solver")
st.markdown("Diagnose business challenges and generate tailored strategies & content with AI.")

st.markdown("---")
st.header("📝 Step 1: Business Information")

# Form Inputs
business_name = st.text_input("Business Name", placeholder="e.g., EcoFashion Co.")
industry = st.text_input("Industry", placeholder="e.g., Fashion, Tech")
target_audience = st.text_input("Target Audience", placeholder="e.g., Gen Z women")
business_goal = st.text_input("Business Goal", placeholder="e.g., Improve sales conversion")
problem = st.text_area("Describe the Current Problem", placeholder="e.g., Sales dropped 30% despite marketing efforts.")

# Submit Button
if st.button("🧠 Diagnose Problem"):
    with st.spinner("🔍 Sending to Gemini..."):
        try:
            model = genai.GenerativeModel("gemini-pro")
            prompt = f"""
You are an AI business growth strategist.

Analyze the business context and suggest solutions in three sections:
1. Diagnosis Summary
2. Strategic Suggestions
3. AI-Powered Content Ideas

Business Name: {business_name}
Industry: {industry}
Target Audience: {target_audience}
Business Goal: {business_goal}
Problem: {problem}
"""
            response = model.generate_content(prompt)
            st.markdown("---")
            st.subheader("📊 Diagnosis Result")
            st.write(response.text)
        except Exception as e:
            st.error(f"❌ Gemini API Error:\n\n{e}")
