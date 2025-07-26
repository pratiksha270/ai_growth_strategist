import streamlit as st

# ---- Page Config ----
st.set_page_config(page_title="AI Growth Strategist", layout="centered")

# ---- Custom Styling ----
st.markdown("""
    <style>
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        .stTextInput>div>div>input {
            background-color: #1e1e2f;
            color: #ffffff;
        }
        .stTextArea>div>textarea {
            background-color: #1e1e2f;
            color: #ffffff;
        }
        .stButton>button {
            background-color: #FF4B4B;
            color: white;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# ---- Title ----
st.markdown("<h1 style='text-align: center;'>🚀 AI Business Growth Strategist & Problem Solver</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Diagnose business challenges and generate tailored strategies & content with AI.</p>", unsafe_allow_html=True)

st.markdown("---")

# ---- Business Info ----
st.header("📋 Step 1: Enter Business Information")

with st.form("business_form"):
    col1, col2 = st.columns(2)
    with col1:
        business_name = st.text_input("Business Name", placeholder="e.g., EcoFashion Co.")
        target_audience = st.text_input("Target Audience", placeholder="e.g., Gen Z women")
    with col2:
        industry = st.text_input("Industry", placeholder="e.g., Fashion, Tech")
        business_goal = st.text_input("Business Goal", placeholder="e.g., Improve sales conversion")

    problem_statement = st.text_area("Describe the Current Problem", placeholder="e.g., Sales dropped 30% despite marketing efforts.")

    submitted = st.form_submit_button("Submit Details")

# ---- Step 2: AI Modules (Placeholder for Day 2) ----
if submitted:
    st.success("✅ Details submitted. Proceed to analysis below.")

    st.markdown("---")
    st.header("🧠 Step 2: AI Strategy & Content")
    
    col3, col4, col5 = st.columns(3)
    with col3:
        if st.button("🔍 Diagnose Problem"):
            st.info("Diagnosis module will analyze your business issue here. [Coming Tomorrow]")
    with col4:
        if st.button("📈 Generate 30-60-90 Strategy"):
            st.info("AI will suggest a strategic roadmap. [Coming Soon]")
    with col5:
        if st.button("✍️ Generate Content"):
            st.info("AI will generate email and social content. [Coming Soon]")

st.markdown("---")
st.caption("🛠️ Prototype v0.2 | Designed for Streamlit Cloud | Updated UI with custom layout")
