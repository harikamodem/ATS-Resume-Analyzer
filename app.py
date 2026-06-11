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
from utils.project_detector import (
    detect_projects
)
from utils.project_score import (
    project_score
)
from utils.project_feedback import (
    project_feedback
)
from utils.experience_detector import (
    detect_experience
)
from utils.experience_score import (
    experience_score
)
from utils.career_score import (
    career_score
)
from utils.education_detector import (
    detect_education
)
from utils.education_score import (
    education_score
)
from utils.cgpa_detector import (
    detect_cgpa
)
from utils.cgpa_rating import (
    cgpa_rating
)
from utils.resume_ranker import (
    resume_ranker
)
from utils.hiring_decision import (
    hiring_decision
)
from utils.report_generator import (
    generate_report
)
from utils.name_extractor import (
    extract_name
)
from utils.keyword_density import (
    keyword_density
)
from utils.benchmark import (
    benchmark_score
)
from utils.ats_optimizer import (
    ats_optimizer
)
from utils.risk_detector import (
    risk_detector
)
from utils.recruiter_dashboard import (
    recruiter_dashboard
)
from utils.achievement_detector import (
    detect_achievements
)
from utils.impact_score import (
    impact_score
)
from utils.action_verbs import (
    action_verbs
)
from utils.achievement_rating import (
    achievement_rating
)
from utils.achievement_chart import (
    achievement_chart
)
from utils.strengths_analyzer import (
    analyze_strengths
)
from utils.weaknesses_analyzer import (
    analyze_weaknesses
)
from utils.candidate_profile import (
    candidate_profile
)
from utils.technical_score import (
    technical_score
)
from utils.swot_analysis import (
    swot_analysis
)
from utils.recruiter_summary import (
    recruiter_summary
)
from utils.batch_analyzer import (
    batch_analyzer
)
from utils.candidate_comparator import (
    candidate_comparator
)
from utils.shortlist_engine import (
    shortlist_engine
)
from utils.leaderboard_chart import (
    leaderboard_chart
)
from utils.resume_pipeline import (
    resume_pipeline
)
from utils.batch_processor import (
    batch_processor
)
from utils.top_candidates import (
    top_candidates
)
from utils.hiring_pipeline import (
    hiring_pipeline
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

multiple_resumes = st.file_uploader(
    "Upload Multiple Resumes",
    type = ["pdf"],
    accept_multiple_files=True
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

    candidate_name = extract_name(
        text
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

    project_count = detect_projects(
        text
    )

    st.subheader(
        "Resume Statistics"
    )

    st.metric(
        "Projects Found",
        project_count
    )

    proj_score = project_score(
        project_count
    )

    st.subheader(
        "Project Strength"
    )

    st.metric(
        "Project Score",
        f"{proj_score}%"
    )

    st.info(
        project_feedback(
            proj_score
        )
    )

    experience_count = detect_experience(
        text
    )

    st.subheader(
        "Experience Analysis"
    )

    st.metric(
        "Experience Indicators",
        experience_count
    )

    exp_score = experience_score(
        experience_count
    )

    st.metric(
        "Experience Score",
        f"{exp_score}%"
    )

    career = career_score(
        proj_score,
        exp_score
    )

    st.subheader(
        "Career Readiness"
    )

    st.metric(
        "Career Score",
        f"{career}%"
    )

    achievement_count = (
        detect_achievements(
            text
        )
    )

    st.subheader(
        "Achievement Analysis"
    )

    st.metric(
        "Achievements Found",
        achievement_count
    )

    impact = impact_score(
        achievement_count
    )

    st.metric(
        "Impact Score",
        f"{impact}%"
    )

    st.success(
        achievement_rating(
            impact
        )
    )

    verbs = action_verbs()

    st.subheader(
        "Action Verb Analysis"
    )

    for verb in verbs:
        count = text.lower().count(
            verb
        )
        if count > 0:
            st.write(
                f"{verb}: {count}"
            )

    chart = achievement_chart(
        impact
    )

    st.plotly_chart(
        chart,
        use_container_width=True
    )
    
    cgpa = detect_cgpa(
        text
    )

    st.subheader(
        "CGPA Analysis"
    )

    if cgpa:
        st.metric(
            "CGPA",
            cgpa
        )
        
        st.success(
            cgpa_rating(
                cgpa
            )
        )

    else:
        st.warning(
            "CGPA Not Found"
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

    education = detect_education(
        text
    )

    st.subheader(
        "Education Analysis"
    )

    for item in education:
        st.success(
            item.upper()
        )

    edu_score = education_score(
        education
    )

    st.metric(
        "Education Score",
        f"{edu_score}%"
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

    st.subheader(
        "Keyword Density"
    )

    for skill, count in top_skills:
        if count > 0:
            density = keyword_density(
            cleaned_resume,
            skill
        )
            
            st.write(
                f"{skill} → {density}%"
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

    status, average = benchmark_score(
        score
    )

    st.subheader(
       "Industry Benchmark"
    )

    st.metric(
        "Industry Average",
        f"{average}%"
    )

    st.success(
        status
    )
    
    st.caption(
        "Weighted ATS Score"
    )

    st.subheader(
       "Semantic Match Score"
    )

    st.metric(
        "AI Similarity",
        f"{semantic_score:.1f}%"
    )

    risks = risk_detector(
        score,
        semantic_score
    )

    st.subheader(
        "Recruiter Risk Flags"
    )

    for risk in risks:
        st.error(
            risk
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

    optimizer = ats_optimizer(
        score,
        missing_skills
    )

    st.subheader(
        "ATS Optimization"
    )
    for item in optimizer:
        st.warning(
            item
        )
    
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

    final_rank = (
        score +
        semantic_score +
        career +
        edu_score +
        impact
    ) / 5

    strengths = analyze_strengths(
        score,
        semantic_score,
        proj_score,
        impact
    )

    st.subheader(
        "Resume Strengths"
    )

    for item in strengths:
        st.success(
            item
        )

    weaknesses = analyze_weaknesses(
        score,
        missing_skills,
        exp_score
    )

    st.subheader(
        "Resume Weaknesses"
    )

    for item in weaknesses:
        st.warning(
            item
        )

    profile = candidate_profile(
        career,
        impact,
        semantic_score
    )

    st.subheader(
        "Candidate Profile"
    )

    st.info(
        profile
    )

    tech_score = technical_score(
        score,
        semantic_score,
        proj_score
    )

    st.subheader(
        "Technical Profile"
    )

    st.metric(
        "Technical Score",
        f"{tech_score}%"
    )

    swot = swot_analysis(
        strengths,
        weaknesses
    )

    st.subheader(
        "SWOT Analysis"
    )

    for key, values in swot.items():
        st.write(
            f"### {key}"
        )

        for item in values:
            st.write(
                f"• {item}"
            )
    
    summary = recruiter_summary(
        profile,
        final_rank
    )

    st.subheader(
        "Recruiter Summary"
    )

    st.info(
        summary
    )
    
    dashboard = recruiter_dashboard(
        score,
        semantic_score,
        career,
        edu_score,
        final_rank
    )

    st.subheader(
        "Recruiter Dashboard"
    )

    st.plotly_chart(
        dashboard,
        use_container_width=True
    )

    st.subheader(
        "Resume Ranking"
    )

    st.metric(
        "Overall Rank Score",
        f"{final_rank}%"
    )

    st.subheader(
    "Hiring Recommendation"
    )
   
    st.success(
        hiring_decision(
            final_rank
        )
    )

    if multiple_resumes:
        st.subheader(
            "Batch Resume Analysis"
        )

        skill_db = load_skills(
            "data/skills.txt"
        )

        candidates = batch_processor(
            multiple_resumes,
            job_description,
            skill_db,
            extract_text_from_pdf
        )

        candidates = sorted(
            candidates,
            key=lambda x: x["score"],
            reverse=True
        )

        st.subheader(
            "Candidate Leaderboard"
        )

        for i, candidate in enumerate(
            candidates,
            start=1
        ):
            st.write(
                f"{i}. "
                f"{candidate['name']} "
                f"({candidate['score']}%)"
            )

        top3 = top_candidates(
            candidates
        )

        st.subheader(
            "Top 3 Candidates"
        )

        for candidate in top3:
            st.success(
                candidate["name"]
            )

        st.subheader(
            "Hiring Pipeline"
        )

        for candidate in candidates:
            stage = hiring_pipeline(
                candidate["score"]
            )

            st.write(
                f"{candidate['name']} → {stage}"
            )

        chart = leaderboard_chart(
            [
                {
                    "name": c["name"],
                    "rank": c["score"]
                }
                for c in candidates
            ]
        )

        st.plotly_chart(
            chart,
            use_container_width=True
        )


    if st.button(
        "Generate PDF Report"
    ):
        decision = hiring_decision(
            final_rank
        )

        generate_report(
            candidate_name,    
            score,
            semantic_score,
            grade,
            final_rank,
            decision,
            list(resume_skills),
            list(missing_skills),
            recommendations,
            career,
            edu_score,
            impact,
            profile,
            tech_score
        )

        st.success(
             "Report Generated"
        )

    with open(
        "report.pdf",
        "rb"
    ) as file:

        st.download_button(
            "Download Report",
            file,
            file_name="Resume_Report.pdf"
        )



     