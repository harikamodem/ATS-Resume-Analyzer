def resume_ranker(
        ats,
        semantic,
        career,
        education):

    return round(
        (
            ats +
            semantic +
            career +
            education
        ) / 4,
        2
    )