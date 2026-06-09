from data.skill_weights import (
    SKILL_WEIGHTS
)
def get_importance(
        jd_skills):
    result = {}
    for skill in jd_skills:
        result[skill] = (
            SKILL_WEIGHTS.get(
                skill,
                1
            )
        )
    return result