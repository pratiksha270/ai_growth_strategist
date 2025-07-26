import streamlit as st
import openai
import os

st.set_page_config(page_title="AI Business Growth Strategist", layout="centered")

# Load API key securely
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("🚀 AI Business Growth Strategist & Problem Solver")
st.caption("Diagnose business challenges and generate tailored strategies & content with AI.")
st.markdown("---")

# STEP 1: Business Info Form
with st.form("business_info"):
    st.subheader("📝 Step 1: Enter Business Information")

    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Business Name", placeholder="e.g., EcoFashion Co.")
        audience = st.text_input("Target Audience", placeholder="e.g., Gen Z women")
    with col2:
        industry = st.text_input("Industry", placeholder="e.g., Fashion, Tech")
        goal = st.text_input("Business Goal", placeholder="e.g., Improve sales conversion")

    problem = st.text_area("Describe the Current Problem", placeholder="e.g., Sales dropped 30% despite marketing efforts.")

    submitted = st.form_submit_button("Submit Details")

# Store input to session state
if submitted:
    st.session_state.submitted = True
    st.session_state.inputs = {
        "name": name,
        "industry": industry,
        "audience": audience,
        "goal": goal,
        "problem": problem
    }
    st.success("✅ Details submitted. Scroll down to analyze the problem.")

# STEP 2: Diagnosis
if st.session_state.get("submitted"):
    st.markdown("---")
    st.subheader("🔍 Step 2: Diagnose the Business Problem")

    if st.button("Diagnose Problem"):
        with st.spinner("Analyzing business issues using AI..."):
            prompt = f"""
You are an expert business consultant. Analyze the following business context and identify possible causes of the described problem.
Categorize the causes into:
- Product Issues
- Marketing Issues
- External Factors

Business Name: {name}
Industry: {industry}
Target Audience: {audience}
Business Goal: {goal}
Problem: {problem}

Present the result as:

📦 Product:
...

📣 Marketing:
...

🌐 External:
...
            """
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7,
                    max_tokens=500
                )
                diagnosis = response['choices'][0]['message']['content']
                st.markdown("### 💡 Diagnosis")
                st.markdown(diagnosis)
            except Exception as e:
                st.error("❌ Failed to get diagnosis. Check your API key or try again later.")
