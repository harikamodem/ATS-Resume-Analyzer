import streamlit as st
from utils.text_cleaner import clean_text
from utils.skill_extractor import extract_skills
st.title("AI Resume Analyzer & ATS Scoring System")
resume = "PYTHON, SQL & MACHINE LEARNING!!!"
cleaned = clean_text(resume)
skill_db = [
    "python",
    "sql",
    "docker",
    "java",
    "machine learning"
]
skills = extract_skills(
    cleaned,
    skill_db
)
st.write("Resume Text")
st.write(resume)
st.write("Extracted Skills")
st.write(skills)