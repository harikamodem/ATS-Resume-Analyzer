from data.skill_aliases import (
    skill_aliases
)
def normalize_skills(
        skill_set):
    normalized = set()
    for skill in skill_set:
        if skill in skill_aliases:
            normalized.add(
                skill_aliases[skill]
            )
        else:
            normalized.add(skill)
    return normalized