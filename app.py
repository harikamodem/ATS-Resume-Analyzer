import streamlit as st

from utils.pdf_parser import extract_text_from_pdf
from utils.text_cleaner import clean_text
from utils.skill_extractor import extract_skills
from utils.ats_scorer import calculate_ats_score

st.title("AI Resume Analyzer & ATS Scoring System")

# Job Description Input
st.subheader("Job Description")

job_description = st.text_area(
    "Paste Job Description Here",
    height=200
)

# Read Resume PDF
text = extract_text_from_pdf(
    "resumes/Modem_Harika_Resume.pdf"
)

# Clean Resume and JD
cleaned_resume = clean_text(text)
cleaned_jd = clean_text(job_description)

# Skills Database
skill_db = [
    "python",
    "c",
    "c++",
    "tensorflow",
    "keras",
    "pytorch",
    "numpy",
    "pandas",
    "matlab",
    "langchain",
    "autocad",
    "excel",
    "sql",
    "git",
    "docker",
    "machine learning",
    "deep learning"
]

# Extract Skills
resume_skills = set(
    extract_skills(
        cleaned_resume,
        skill_db
    )
)

jd_skills = set(
    extract_skills(
        cleaned_jd,
        skill_db
    )
)

# ATS Score
score = calculate_ats_score(
    resume_skills,
    jd_skills
)

# Display Resume Skills
st.subheader("Resume Skills")

for skill in resume_skills:
    st.write("✅", skill)

# Display JD Skills
st.subheader("Job Description Skills")

for skill in jd_skills:
    st.write("📌", skill)

# Display ATS Score
st.subheader("ATS Score")

st.metric(
    "Match Percentage",
    f"{score:.1f}%"
)

# Matched Skills
matched_skills = resume_skills.intersection(
    jd_skills
)

st.subheader("Matched Skills")

for skill in matched_skills:
    st.write("✅", skill)

# Missing Skills
missing_skills = jd_skills - resume_skills

st.subheader("Missing Skills")

for skill in missing_skills:
    st.write("❌", skill)

# Recommendations
st.subheader("Recommendations")

for skill in missing_skills:
    st.write(
        "👉 Add",
        skill,
        "to your resume"
    )

# Resume Grade
if score >= 80:
    grade = "Excellent"

elif score >= 60:
    grade = "Good"

elif score >= 40:
    grade = "Average"

else:
    grade = "Needs Improvement"

st.subheader("Resume Grade")

st.success(grade)