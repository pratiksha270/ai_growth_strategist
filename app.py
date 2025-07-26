import streamlit as st
import google.generativeai as genai
import os
import json
import time

# Load credentials from secrets
service_account_info = json.loads(st.secrets["GOOGLE_SERVICE_ACCOUNT_JSON"])

# Configure Gemini
genai.configure(service_account=service_account_info)

# Load model
model = genai.GenerativeModel("gemini-pro")

st.set_page_config(page_title="AI Business Growth Strategist", layout="centered")

st.title("🚀 AI Business Growth Strategist & Problem Solver")
st.write("Diagnose business challenges and generate tailored strategies & content with AI.")

# Step 1: Business Info Input
st.header("📝 Step 1: Business Information")
business_name = st.text_input("Business Name")
industry = st.text_input("Industry")
target_audience = st.text_input("Target Audience")
business_goal = st.text_input("Business Goal")
problem = st.text_area("Describe the Current Problem")

if st.button("🧠 Diagnose Problem"):
    if not all([business_name, industry, target_audience, business_goal, problem]):
        st.warning("⚠️ Please fill in all fields.")
    else:
        prompt = f"""You are a Business Growth Strategist AI.
Business Name: {business_name}
Industry: {industry}
Target Audience: {target_audience}
Business Goal: {business_goal}
Current Problem: {problem}

Generate a diagnosis of the problem and give a detailed strategy, growth roadmap, and tailored marketing suggestions."""
        
        with st.spinner("🔍 Sending to Gemini..."):
            try:
                start = time.time()
                response = model.generate_content(prompt)
                duration = round(time.time() - start, 2)

                st.success("✅ Gemini responded successfully!")
                st.markdown(f"⏱️ Response time: {duration} seconds")
                st.subheader("📈 Strategy Recommendation")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"❌ Gemini API Error:\n\n{str(e)}")
