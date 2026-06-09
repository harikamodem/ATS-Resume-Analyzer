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
from utils.resume_stats import (
    resume_stats
)
from utils.quality_checker import (
    quality_check
)

st.title("AI Resume Analyzer & ATS Scoring System")

st.subheader("Upload Resume")

# Job Description Input
st.subheader("Job Description")

job_description = st.text_area(
    "Paste Job Description Here",
    height=200
)

st.subheader(
    "Upload Job Description PDF"
)

jd_file = st.file_uploader(
    "Choose JD PDF",
    type=["pdf"]
)

uploaded_file = st.file_uploader(
    "Choose Resume PDF",
    type=["pdf"]
) 

if uploaded_file:
    with open(
        "uploads/resume.pdf",
        "wb"
    ) as f:
        f.write(
            uploaded_file.getbuffer()
        )
    text = extract_text_from_pdf(
        "uploads/resume.pdf"
    )
    st.success(
        "Resume uploaded successfully."
    )
    st.subheader(
        "Resume Preview"
    )

    st.success(
        "Resume analyzed successfully."
    )
    st.text_area(
    "Extracted Text",
    text[:2000],
    height=250
    )
    words, chars = resume_stats(
    text
    )

    st.subheader(
        "Resume Statistics"
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Words",
            words
        )

    with col2:
        st.metric(
        "Characters",
        chars
        )

    quality = quality_check(
    words
    )

    st.subheader(
        "Resume Quality"
    )

    st.info(
        quality
    )

    if jd_file:

        with open(
        "uploads/jd.pdf",
        "wb"
        ) as f:

            f.write(
            jd_file.getbuffer()
            )

        job_description = extract_text_from_pdf(
        "uploads/jd.pdf"
        )

    cleaned_resume = clean_text(text)
    cleaned_jd = clean_text(job_description)

    skill_db = load_skills(
        "data/skills.txt"
    )

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

    resume_skills = normalize_skills(
    resume_skills
    )
    jd_skills = normalize_skills(
    jd_skills
    )

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

    score = calculate_ats_score(
    resume_skills,
    jd_skills
    )

    st.subheader("ATS Score")

    st.metric(
    "Match Percentage",
    f"{score:.1f}%"
    )

    chart = create_score_chart(score)

    st.plotly_chart(
    chart,
    use_container_width=True
    )

    st.subheader("Job Description Skills")

    for skill in jd_skills:
        st.write("📌", skill)

    matched_skills = resume_skills.intersection(
    jd_skills
    )

    st.subheader("Matched Skills")

    for skill in matched_skills:
        st.write("✅", skill)

    missing_skills = jd_skills - resume_skills

    st.subheader("Missing Skills")

    for skill in missing_skills:
        st.write("❌", skill)

    pie_chart = create_match_chart(
    matched_skills,
    missing_skills
    )
    st.plotly_chart(
    pie_chart,
    use_container_width=True
    )

    recommendations = generate_recommendations(
    missing_skills
    )
    st.subheader("Recommendations")
    for recommendation in recommendations:
        st.write("👉", recommendation)

    feedback = generate_feedback(
    score
    )

    st.subheader(
    "ATS Feedback"
    )
    st.info(feedback)

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



