import streamlit as st
import openai
import os

# --- Configuration ---
st.set_page_config(page_title="AI Business Growth Strategist", layout="centered")

# Set and test OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")
st.write("✅ API Key Loaded:", bool(openai.api_key))  # ✅ Debug print

# --- Title ---
st.title("🚀 AI Business Growth Strategist & Problem Solver")
st.caption("Diagnose business challenges and generate tailored strategies & content with AI.")
st.markdown("---")

# --- Step 1: Business Information ---
st.subheader("📝 Step 1: Enter Business Information")

col1, col2 = st.columns(2)
with col1:
    name = st.text_input("Business Name", placeholder="e.g., EcoFashion Co.")
    audience = st.text_input("Target Audience", placeholder="e.g., Gen Z women")
with col2:
    industry = st.text_input("Industry", placeholder="e.g., Fashion, Tech")
    goal = st.text_input("Business Goal", placeholder="e.g., Improve sales conversion")

problem = st.text_area("Describe the Current Problem", placeholder="e.g., Sales dropped 30% despite marketing efforts.")
st.markdown("")

# --- Diagnose Function ---
def diagnose_problem(name, industry, audience, goal, problem):
    prompt = f"""
You are an expert business strategist. A business needs help.

Business Name: {name}
Industry: {industry}
Target Audience: {audience}
Business Goal: {goal}
Current Problem: {problem}

Diagnose the problem and categorize it as:
- Product-related
- Marketing-related
- External (e.g., economic, seasonal)

Explain clearly and suggest 2-3 focus areas.
"""

    try:
        st.write("🔍 Sending to OpenAI...")  # ✅ Debug print
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"❌ OpenAI API Error: {e}")
        return None

# --- Diagnose Button ---
if st.button("Diagnose Problem"):
    st.write("📨 Diagnose Button Clicked")  # ✅ Debug print
    with st.spinner("Analyzing business problem..."):
        diagnosis = diagnose_problem(name, industry, audience, goal, problem)
        if diagnosis:
            st.success("✅ Diagnosis Complete")
            st.markdown(diagnosis)
        else:
            st.error("❌ Failed to fetch diagnosis.")
