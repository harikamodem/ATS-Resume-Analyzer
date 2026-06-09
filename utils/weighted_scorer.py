from data.skill_weights import (
    SKILL_WEIGHTS
)

def weighted_score(
        resume_skills,
        jd_skills):

    total_weight = 0
    matched_weight = 0

    for skill in jd_skills:

        weight = SKILL_WEIGHTS.get(
            skill,
            1
        )

        total_weight += weight

        if skill in resume_skills:
            matched_weight += weight

    if total_weight == 0:
        return 0

    return (
        matched_weight /
        total_weight
    ) * 100