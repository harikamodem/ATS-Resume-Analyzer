def education_score(
        education):

    score = len(
        education
    ) * 20

    return min(
        score,
        100
    )