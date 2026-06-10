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
from utils.weighted_scorer import (
    weighted_score
)
from utils.importance import (
    get_importance
)
from utils.critical_skills import (
    critical_missing
)
from utils.weight_chart import (
    weight_chart
)
from utils.score_explainer import (
    explain_score
)
from utils.section_detector import (
    detect_sections
)
from utils.section_score import (
    section_score
)
from utils.structure_grade import (
    structure_grade
)
from utils.missing_sections import (
    missing_sections
)
from utils.section_chart import (
    section_chart
)
from utils.semantic_match import (
    semantic_match
)
from utils.semantic_chart import (
    semantic_chart
)
from utils.semantic_feedback import (
    semantic_feedback
)
from utils.keyword_stuffing import (
    keyword_stuffing
)
from utils.ai_recommendation import (
    ai_recommendation
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

    cleaned_resume = clean_text(text)
    sections = detect_sections(
        text
    )

    section_percentage = section_score(
        sections
    )

    cleaned_jd = clean_text(job_description)

    semantic_score = semantic_match(
        text,
        job_description
    )

    chart = semantic_chart(
        semantic_score
    )

    st.plotly_chart(
        chart,
        use_container_width=True
    )

    st.subheader(
        "AI Analysis"
    )

    st.info(
        semantic_feedback(
            semantic_score
        )
    )

    st.subheader(
        "AI Recommendation"
    )

    st.success(
        ai_recommendation(
            semantic_score
        )
    )

    st.subheader(
        "Resume Sections"
    )

    for section, present in sections.items():

        if present:

            st.success(
                f"{section} Found"
            )

        else:

            st.error(
                f"{section} Missing"
            )

    st.subheader(
        "Resume Structure Score"
    )

    st.metric(
        "Section Completeness",
        f"{section_percentage:.1f}%"
    )

    st.success(
        structure_grade(
            section_percentage
        )
    )

    missing = missing_sections(
        sections
    )

    st.subheader(
        "Missing Resume Sections"
    )

    for item in missing:

        st.warning(
            item
        )

    chart = section_chart(
        sections
    )

    st.plotly_chart(
        chart,
        use_container_width=True
    )

    if len(missing) > 0:

       st.subheader(
           "Structure Recommendations"
       )

       for item in missing:

            st.write(
                f"Add {item} section"
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

    cleaned_jd = clean_text(
        job_description
    )

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

    if keyword_stuffing(
        keyword_counts
    ):
        st.warning(
            "Possible keyword stuffing detected."
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
    
    score = weighted_score(
        resume_skills,
        jd_skills
    )

    st.subheader("ATS Score")

    st.metric(
        "Match Percentage",
        f"{score:.1f}%"
    )
    
    st.caption(
        "Weighted ATS Score"
    )

    semantic_score = semantic_match(
        text,
        job_description
    )

    st.subheader(
       "Semantic Match Score"
    )

    st.metric(
        "AI Similarity",
        f"{semantic_score:.1f}%"
    )
    
    st.subheader(
        "ATS vs AI Match"
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "ATS Score",
            f"{score:.1f}%"
        )

    with col2:
        st.metric(
            "AI Score",
            f"{semantic_score:.1f}%"
        )

    gauge_chart = create_score_chart(
        score
    )

    st.plotly_chart(
        gauge_chart,
        use_container_width=True
    )

    st.subheader("Job Description Skills")

    for skill in jd_skills:
        st.write("📌", skill)
    
    importance = get_importance(
        jd_skills
    )

    st.subheader(
        "Skill Importance"
    )

    for skill, weight in importance.items():
        st.write(
            f"{skill} → {weight} points"
        )
    
    chart = weight_chart(
        importance
    )
    st.plotly_chart(
        chart,
        use_container_width=True
    )

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
    
    critical = critical_missing(
        missing_skills
    )

    st.subheader(
        "Critical Missing Skills"
    )

    for skill in critical:
        st.error(
            f"High Priority: {skill}"
        )


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
    
    st.subheader(
        "Score Interpretation"
    )

    st.info(
        explain_score(
            score
        )
    )

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

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



