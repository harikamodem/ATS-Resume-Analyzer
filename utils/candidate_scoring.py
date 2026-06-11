def candidate_scoring(
    ats,
    semantic
):

    return round(
        (
            ats +
            semantic
        ) / 2,
        2
    )