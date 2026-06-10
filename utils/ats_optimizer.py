def ats_optimizer(
    score,
    missing_skills
):

    suggestions = []

    if score < 70:

        suggestions.append(
            "Increase skill coverage."
        )

    if len(missing_skills) > 0:

        suggestions.append(
            "Add missing JD skills."
        )

    if score < 50:

        suggestions.append(
            "Rewrite resume for ATS compatibility."
        )

    return suggestions