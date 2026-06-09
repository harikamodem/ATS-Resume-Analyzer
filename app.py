import streamlit as st

from utils.pdf_parser import extract_text_from_pdf
from utils.text_cleaner import clean_text
from utils.skill_extractor import extract_skills
from utils.ats_scorer import calculate_ats_score
from utils.skill_loader import load_skills
from utils.skill_categorizer import categorize_skills
from utils.skill_normalizer import normalize_skills
from utils.recommendation_engine import generate_recommendations
from utils.charts import create_score_chart
from utils.keyword_analyzer import (
    keyword_count
)
from utils.strengths import (
    strongest_skills
)
from utils.feedback_engine import (
    generate_feedback
)
from utils.match_chart import (
    create_match_chart
)

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
skill_db = load_skills(
    "data/skills.txt"
)

#keywords
keyword_counts = keyword_count(
    cleaned_resume,
    skill_db
)

st.subheader(
    "Keyword Frequency"
)
st.write(
    keyword_counts
)

top_skills = strongest_skills(
    keyword_counts
)

st.subheader(
    "Top Skills"
)

for skill, count in top_skills:
    if count > 0:
        st.write(
            f"⭐ {skill} ({count})"
        )

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

#normalize skills
resume_skills = normalize_skills(
    resume_skills
)
jd_skills = normalize_skills(
    jd_skills
)

# Display Resume Skills
st.subheader("Resume Skills")

for skill in resume_skills:
    st.write("✅", skill)


categorized = categorize_skills(
    resume_skills
)

st.subheader("Skill Categories")

for category in categorized:
    st.write(category)
    for skill in categorized[category]:
        st.write("•", skill)

# ATS Score
score = calculate_ats_score(
    resume_skills,
    jd_skills
)
# Display ATS Score
st.subheader("ATS Score")

st.metric(
    "Match Percentage",
    f"{score:.1f}%"
)

#chart
chart = create_score_chart(score)

st.plotly_chart(
    chart,
    use_container_width=True
)

# Display JD Skills
st.subheader("Job Description Skills")

for skill in jd_skills:
    st.write("📌", skill)


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

#pie chart
pie_chart = create_match_chart(
    matched_skills,
    missing_skills
)
st.plotly_chart(
    pie_chart,
    use_container_width=True
)

# Recommendations
recommendations = generate_recommendations(
    missing_skills
)
st.subheader("Recommendations")
for recommendation in recommendations:
    st.write("👉", recommendation)

# Feedback
feedback = generate_feedback(
    score
)

st.subheader(
    "ATS Feedback"
)
st.info(feedback)

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

# Dashboard
col1, col2 = st.columns(2)
with col1:
    st.metric(
        "ATS Score",
        f"{score:.1f}%"
    )
with col2:
    st.success(
        grade
    )