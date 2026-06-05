from utils.skill_extractor import extract_skills

resume_text = "python sql machine learning"

skill_db = [
    "python",
    "sql",
    "docker",
    "git",
    "machine learning"
]

resume_skills = set(
    extract_skills(
        resume_text,
        skill_db
    )
)

jd_skills = {
    "python",
    "sql",
    "docker",
    "git"
}

matched = resume_skills.intersection(jd_skills)

score = (len(matched) / len(jd_skills)) * 100

print("Resume Skills:", resume_skills)
print("JD Skills:", jd_skills)
print("Matched Skills:", matched)
print("ATS Score:", score)