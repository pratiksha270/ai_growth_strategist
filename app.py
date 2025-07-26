import streamlit as st
import google.generativeai as genai
import os

# Load API key from secrets
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]

# Configure Gemini with API key
genai.configure(api_key=GOOGLE_API_KEY)

# Set up Gemini model
model = genai.GenerativeModel("gemini-pro")

# Streamlit app UI
st.set_page_config(page_title="AI Business Growth Strategist", layout="centered")

st.title("🚀 AI Business Growth Strategist & Problem Solver")
st.caption("Diagnose business challenges and generate tailored strategies & content with AI.")

with st.form("business_form"):
    st.subheader("📝 Step 1: Business Information")

    business_name = st.text_input("Business Name", placeholder="e.g., EcoFashion Co.")
    industry = st.text_input("Industry", placeholder="e.g., Fashion, Tech")
    target_audience = st.text_input("Target Audience", placeholder="e.g., Gen Z women")
    business_goal = st.text_input("Business Goal", placeholder="e.g., Improve sales conversion")
    problem = st.text_area("Describe the Current Problem", placeholder="e.g., Sales dropped 30% despite marketing efforts.")

    submitted = st.form_submit_button("🧠 Diagnose Problem")

if submitted:
    if not all([business_name, industry, target_audience, business_goal, problem]):
        st.warning("Please fill in all the fields before submitting.")
    else:
        with st.spinner("🔍 Sending to Gemini..."):
            prompt = f"""
            Business Name: {business_name}
            Industry: {industry}
            Target Audience: {target_audience}
            Business Goal: {business_goal}
            Problem: {problem}

            As a business growth strategist, analyze the above context and generate:
            1. Root cause of the issue
            2. Strategic solutions
            3. Marketing ideas
            4. Growth roadmap
            """

            try:
                response = model.generate_content(prompt)
                st.success("✅ Strategy Generated!")
                st.markdown(response.text)

            except Exception as e:
                st.error(f"❌ Gemini API Error:\n\n{str(e)}")
