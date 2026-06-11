from utils.text_cleaner import clean_text
from utils.skill_extractor import extract_skills
from utils.skill_normalizer import normalize_skills
from utils.weighted_scorer import weighted_score
from utils.semantic_match import semantic_match

def resume_pipeline(
    resume_text,
    jd_text,
    skill_db
):

    cleaned_resume = clean_text(
        resume_text
    )

    cleaned_jd = clean_text(
        jd_text
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

    ats = weighted_score(
        resume_skills,
        jd_skills
    )

    if jd_text.strip():
        semantic = semantic_match(
            resume_text,
            jd_text
        )

    else:
        semantic = 0

    return ats, semantic