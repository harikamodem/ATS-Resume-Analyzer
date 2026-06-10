def semantic_feedback(
        score):

    if score >= 80:
        return (
            "Excellent alignment "
            "with job description."
        )

    elif score >= 60:
        return (
            "Good match with "
            "job requirements."
        )

    elif score >= 40:
        return (
            "Moderate alignment."
        )

    return (
        "Weak alignment."
    )