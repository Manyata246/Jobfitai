import streamlit as st
from resume_parser import extract_text_from_pdf
from ats_score import calculate_ats_score
from resume_generator import get_improvement_suggestions, generate_resume

st.set_page_config(page_title="Resume ATS Evaluator", layout="wide")

st.title("🧠 Resume RAG-based ATS Evaluator")

uploaded_file = st.file_uploader("📤 Upload your resume (PDF)", type=["pdf"])

if uploaded_file:
    text = extract_text_from_pdf(uploaded_file)
    st.subheader("📄 Extracted Resume Text")
    st.text_area("Resume Text", text, height=300)

    # ATS Score
    score = calculate_ats_score(text)
    st.subheader(f"📊 ATS Score: {score:.2f}%")

    if st.button("💡 Get Improvement Suggestions"):
        suggestions = get_improvement_suggestions(text)
        st.subheader("✍️ Suggestions")
        st.write(suggestions)

st.markdown("---")
st.subheader("📝 Generate Resume from Details")

with st.form("resume_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    education = st.text_area("Education")
    experience = st.text_area("Experience")
    skills = st.text_area("Skills")
    submitted = st.form_submit_button("🚀 Generate Resume")

if submitted:
    inputs = {
        "name": name,
        "email": email,
        "phone": phone,
        "education": education,
        "experience": experience,
        "skills": skills
    }
    result = generate_resume(inputs)
    st.subheader("🧾 Generated Resume")
    st.write(result)
