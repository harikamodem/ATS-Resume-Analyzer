def career_score(
        project_score,
        exp_score):

    return round(
        (
            project_score +
            exp_score
        ) / 2,
        2
    )