def technical_score(
    ats,
    semantic,
    projects
):

    return round(
        (
            ats +
            semantic +
            projects
        ) / 3,
        2
    )