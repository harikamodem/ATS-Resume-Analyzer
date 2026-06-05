def generate_recommendations(
        missing_skills):
    recommendations = []
    for skill in missing_skills:
        recommendations.append(
            f"Consider learning "
            f"{skill} and adding "
            f"a project using it."
        )
    return recommendations
