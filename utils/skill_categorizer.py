from data.skill_categories import (
    skill_categories
)
def categorize_skills(
        skills):
    result = {}
    for category in skill_categories:
        result[category] = []
        for skill in skills:
            if skill in skill_categories[category]:
                result[category].append(skill)
    return result