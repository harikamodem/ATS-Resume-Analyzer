def analyze_weaknesses(
    score,
    missing_skills,
    experience_score
):

    weaknesses = []

    if score < 70:
        weaknesses.append(
            "Low ATS Match"
        )

    if len(missing_skills) > 5:
        weaknesses.append(
            "Many Missing Skills"
        )

    if experience_score < 50:
        weaknesses.append(
            "Limited Experience Indicators"
        )

    return weaknesses
