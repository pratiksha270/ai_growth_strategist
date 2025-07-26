import streamlit as st
import openai
import os

# Config
st.set_page_config(page_title="AI Business Growth Strategist", layout="centered")
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("🚀 AI Business Growth Strategist & Problem Solver")
st.caption("Diagnose business challenges and generate tailored strategies & content with AI.")
st.markdown("---")

# --- Step 1: Business Information ---
st.subheader("📝 Step 1: Business Information")

col1, col2 = st.columns(2)
business_name = col1.text_input("Business Name", placeholder="e.g., EcoFashion Co.")
industry = col2.text_input("Industry", placeholder="e.g., Fashion, Tech")
target_audience = col1.text_input("Target Audience", placeholder="e.g., Gen Z women")
business_goal = col2.text_input("Business Goal", placeholder="e.g., Improve sales conversion")

problem_description = st.text_area("Describe the Current Problem", placeholder="e.g., Sales dropped 30% despite marketing efforts.")

# Button to trigger AI diagnosis
if st.button("🔍 Diagnose Problem"):
    if all([business_name, industry, target_audience, business_goal, problem_description]):
        with st.spinner("Analyzing problem with AI..."):
            prompt = f"""
You are a senior business analyst. A client has provided the following context about their company.

Business Name: {business_name}
Industry: {industry}
Target Audience: {target_audience}
Business Goal: {business_goal}
Current Problem: {problem_description}

Analyze the business problem and categorize causes under:
- 📦 Product Issues
- 📣 Marketing Issues
- 🌐 External Factors

Return the diagnosis clearly under these 3 headings.
"""
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7,
                    max_tokens=500
                )
                diagnosis = response.choices[0].message.content
                st.markdown("---")
                st.subheader("🧠 AI Diagnosis")
                st.markdown(diagnosis)
            except Exception as e:
                st.error("❌ Error fetching response. Check your API key or try again.")
    else:
        st.warning("⚠️ Please fill all fields before diagnosing.")
