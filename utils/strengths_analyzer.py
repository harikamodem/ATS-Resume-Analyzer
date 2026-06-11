def analyze_strengths(
    score,
    semantic_score,
    project_score,
    impact
):

    strengths = []

    if score >= 80:
        strengths.append(
            "Strong ATS Match"
        )

    if semantic_score >= 80:
        strengths.append(
            "Excellent Job Alignment"
        )

    if project_score >= 70:
        strengths.append(
            "Strong Project Portfolio"
        )

    if impact >= 70:
        strengths.append(
            "Quantified Achievements"
        )

    return strengths