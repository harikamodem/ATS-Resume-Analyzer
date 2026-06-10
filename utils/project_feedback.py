def project_feedback(
        score):

    if score >= 80:
        return (
            "Excellent project portfolio."
        )

    elif score >= 60:
        return (
            "Good project experience."
        )

    elif score >= 40:
        return (
            "Add more technical projects."
        )

    return (
        "Projects section is weak."
    )