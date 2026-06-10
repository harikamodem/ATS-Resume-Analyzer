def risk_detector(
    score,
    semantic_score
):

    risks = []

    if score < 60:

        risks.append(
            "Low ATS Match"
        )

    if semantic_score < 60:

        risks.append(
            "Low Semantic Similarity"
        )

    return risks