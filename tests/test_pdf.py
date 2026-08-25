from utils.pdf_parser import extract_text_from_pdf
from utils.text_cleaner import clean_text
from utils.skill_extractor import extract_skills

text = extract_text_from_pdf(
    "resumes/Modem_Harika_Resume.pdf"
)

cleaned = clean_text(text)

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
    "sql",
    "machine learning",
    "deep learning",
    "langchain",
    "autocad",
    "excel"
]

skills = extract_skills(
    cleaned,
    skill_db
)

print(skills)

resume_skills = set(skills)

jd_skills = {
    "python",
    "sql",
    "git",
    "docker",
    "pandas",
    "numpy"
}

matched = resume_skills.intersection(
    jd_skills
)

score = (
    len(matched)
    /
    len(jd_skills)
) * 100

print("Matched:", matched)
print("Score:", score)