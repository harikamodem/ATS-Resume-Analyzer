def hiring_pipeline(
    score
):

    if score >= 85:

        return "Interview"

    elif score >= 70:

        return "Review"

    elif score >= 50:

        return "Hold"

    return "Reject"