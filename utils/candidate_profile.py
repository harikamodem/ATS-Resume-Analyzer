def candidate_profile(
    career,
    impact,
    semantic_score
):

    if (
        career >= 80
        and impact >= 70
    ):
        return "Industry Ready Candidate"

    elif semantic_score >= 80:
        return "Role-Focused Candidate"

    elif career >= 60:
        return "Emerging Professional"

    return "Entry-Level Candidate"