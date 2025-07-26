import streamlit as st
import openai

# Set page config
st.set_page_config(page_title="AI Business Growth Strategist", layout="centered")

# Apply custom styling
st.markdown("""
    <style>
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .stTextInput, .stTextArea {
        background-color: #1e1e1e;
        color: #f5f5f5;
    }
    </style>
""", unsafe_allow_html=True)

# Set OpenAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Title and Description
st.title("🚀 AI Business Growth Strategist & Problem Solver")
st.markdown("Diagnose business challenges and generate tailored strategies & content with AI.")

st.markdown("### 📝 Step 1: Enter Business Information")

# Input fields
with st.form(key="input_form"):
    col1, col2 = st.columns(2)
    with col1:
        business_name = st.text_input("Business Name", placeholder="e.g., EcoFashion Co.")
        target_audience = st.text_input("Target Audience", placeholder="e.g., Gen Z women")
    with col2:
        industry = st.text_input("Industry", placeholder="e.g., Fashion, Tech")
        business_goal = st.text_input("Business Goal", placeholder="e.g., Improve sales conversion")
    
    problem_statement = st.text_area("Describe the Current Problem", placeholder="e.g., Sales dropped 30% despite marketing efforts.")
    
    submitted = st.form_submit_button("Submit Details")

# Function to generate diagnosis
def generate_diagnosis(business_name, industry, audience, goal, problem):
    prompt = f"""
Act as a senior business consultant. The company "{business_name}" operates in the "{industry}" industry. 
Their target audience is "{audience}". Their main goal is: "{goal}". 
They are currently facing this problem: "{problem}".

Analyze the situation and diagnose the possible causes grouped into:
1. Product-related issues
2. Marketing or Sales issues
3. External or market-related issues

Provide the analysis in bullet points under each category.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response['choices'][0]['message']['content']

# If form submitted, show diagnosis section
if submitted:
    st.markdown("---")
    if st.button("🔍 Diagnose Problem"):
        with st.spinner("Analyzing..."):
            diagnosis = generate_diagnosis(
                business_name, industry, target_audience, business_goal, problem_statement
            )
            st.subheader("🧠 Business Problem Diagnosis")
            st.markdown(diagnosis)
