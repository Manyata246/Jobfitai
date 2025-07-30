import streamlit as st
import pdfplumber
from groq import Groq

from groq import Groq

client = Groq(api_key="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")  # Replace with your actual key


# 🧠 Keywords for ATS Scoring
keywords = ["Python", "Machine Learning", "SQL", "NLP", "Git", "Communication", "Teamwork"]

# 📊 Simple ATS Score Calculator
def calculate_score(text):
    score = sum(1 for kw in keywords if kw.lower() in text.lower())
    return (score / len(keywords)) * 100

# ✍️ Suggestions from LLM
def get_suggestions(text):
    response = client.chat.completions.create(
    model="llama3-70b-8192",  # ✅ Updated model name
    messages=[
        {"role": "system", "content": "You are an expert resume writer."},
        {"role": "user", "content": f"Generate a resume using the following details:\n{user_data}"}
    ]


    )
    return response.choices[0].message.content

# 📝 Resume Generator
def generate_resume(data):
    prompt = f"""Create a professional resume with:
Name: {data['name']}
Email: {data['email']}
Phone: {data['phone']}
Education: {data['education']}
Experience: {data['experience']}
Skills: {data['skills']}
Make it ATS-friendly."""
    
    response = client.chat.completions.create(
    model="llama3-70b-8192",  # ✅ Updated model name
    messages=[
        {"role": "system", "content": "You are an expert resume writer."},
        {"role": "user", "content": f"Generate a resume using the following details:\n{user_data}"}
    ]

,
    )
    return response.choices[0].message.content

# 🚀 Streamlit UI
st.title("📄 Jobfitai")
st.subheader("🛠️ Analyze. ✨ Improve. 📝 Generate.")
uploaded = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
if uploaded:
    with pdfplumber.open(uploaded) as pdf:
        text = "\n".join([page.extract_text() for page in pdf.pages])
    st.subheader("Extracted Resume Text")
    st.text_area("Resume Text", text, height=300)

    score = calculate_score(text)
    st.subheader(f"✅ ATS Score: {score:.2f}%")

    if st.button("Get Suggestions"):
        suggestions = get_suggestions(text)
        st.subheader("💡 Improvement Suggestions")
        st.write(suggestions)

st.markdown("---")
st.subheader("🧾 Generate Resume from Details")

with st.form("resume_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    education = st.text_area("Education")
    experience = st.text_area("Experience")
    skills = st.text_area("Skills")
    submitted = st.form_submit_button("Generate Resume")

if submitted:
    user_data = {
        "name": name, "email": email, "phone": phone,
        "education": education, "experience": experience, "skills": skills
    }
    resume = generate_resume(user_data)
    st.subheader("📌 Your Generated Resume")
    st.write(resume)
