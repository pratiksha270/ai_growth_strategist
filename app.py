import streamlit as st
import google.generativeai as genai
import os
import json

# === Load Gemini Credentials ===
# Point this to the downloaded JSON key path
key_path = "geminigrowthapp-230f2d017943.json"  # or st.secrets if on Streamlit Cloud
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_path

# === Configure Gemini ===
genai.configure()

# --- Streamlit UI ---
st.set_page_config(page_title="AI Business Growth Strategist", layout="centered")
st.title("🚀 AI Business Growth Strategist & Problem Solver")
st.caption("Diagnose business challenges and generate tailored strategies & content with AI.")
st.markdown("---")

# Step 1: Business Inputs
st.subheader("📝 Step 1: Business Information")
col1, col2 = st.columns(2)
business_name = col1.text_input("Business Name", placeholder="e.g., EcoFashion Co.")
industry = col2.text_input("Industry", placeholder="e.g., Fashion, Tech")
target_audience = col1.text_input("Target Audience", placeholder="e.g., Gen Z women")
business_goal = col2.text_input("Business Goal", placeholder="e.g., Improve sales conversion")
problem_description = st.text_area("Describe the Current Problem", placeholder="e.g., Sales dropped 30% despite marketing efforts.")

# Diagnose Button
if st.button("🧠 Diagnose Problem"):
    st.info("📨 Diagnose Button Clicked")
    if not problem_description:
        st.warning("Please describe the current problem.")
    else:
        try:
            st.write("🔍 Sending to Gemini...")

            prompt = (
                f"Business Name: {business_name}\n"
                f"Industry: {industry}\n"
                f"Target Audience: {target_audience}\n"
                f"Business Goal: {business_goal}\n"
                f"Current Problem: {problem_description}\n\n"
                "What are the likely reasons for this problem and suggest a growth strategy?"
            )

            model = genai.GenerativeModel("gemini-pro")
            response = model.generate_content(prompt)

            st.success("✅ Diagnosis & Strategy:")
            st.markdown(response.text)

        except Exception as e:
            st.error(f"❌ Gemini API Error:\n\n{e}")
