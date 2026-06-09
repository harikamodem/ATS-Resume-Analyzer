from data.skill_weights import (
    SKILL_WEIGHTS
)
def critical_missing(
        missing_skills):
    result = []
    for skill in missing_skills:
        if (
            SKILL_WEIGHTS.get(
                skill,
                1
            ) >= 8
        ):
            result.append(skill)
    return result