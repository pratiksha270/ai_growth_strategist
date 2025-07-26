import streamlit as st
import google.generativeai as genai
import os
import json

# Set up page config
st.set_page_config(page_title="AI Business Growth Strategist", page_icon="🚀", layout="centered")

# Set environment variable for credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "geminigrowthapp-230f2d017943.json"

# Initialize Gemini
genai.configure()
model = genai.GenerativeModel("gemini-pro")

# App UI
st.title("🚀 AI Business Growth Strategist & Problem Solver")
st.markdown("Diagnose business challenges and generate tailored strategies & content with AI.")

st.subheader("📝 Step 1: Business Information")
business_name = st.text_input("Business Name", placeholder="e.g., EcoFashion Co.")
target_audience = st.text_input("Target Audience", placeholder="e.g., Gen Z women")
industry = st.text_input("Industry", placeholder="e.g., Fashion, Tech")
business_goal = st.text_input("Business Goal", placeholder="e.g., Improve sales conversion")
problem_description = st.text_area("Describe the Current Problem", placeholder="e.g., Sales dropped 30% despite marketing efforts.")

if st.button("🧠 Diagnose Problem"):
    if not all([business_name, target_audience, industry, business_goal, problem_description]):
        st.warning("Please fill out all fields before proceeding.")
    else:
        with st.spinner("🔍 Sending to Gemini..."):
            try:
                prompt = f"""
                I am a business analyst. Here is the company info:

                Business Name: {business_name}
                Target Audience: {target_audience}
                Industry: {industry}
                Business Goal: {business_goal}
                Current Problem: {problem_description}

                Based on the above, generate:
                1. Root cause analysis of the business problem
                2. 3 tailored growth strategies
                3. 2 AI tools that could be used to help
                4. Suggested campaign ideas with channels (email, Instagram, etc)
                5. A motivational business insight quote
                """

                response = model.generate_content(prompt)
                st.success("✅ Diagnosis Complete!")
                st.markdown(response.text)

            except Exception as e:
                st.error(f"❌ Gemini API Error:\n\n{e}")
