def ai_recommendation(
        semantic_score):

    if semantic_score < 50:

        return (
            "Add more relevant "
            "project and skill details."
        )

    elif semantic_score < 70:

        return (
            "Improve alignment "
            "with JD terminology."
        )

    return (
        "Strong semantic match."
    )