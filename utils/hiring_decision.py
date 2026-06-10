def hiring_decision(
        score):

    if score >= 85:
        return "Strong Hire"

    elif score >= 70:
        return "Hire"

    elif score >= 55:
        return "Consider"

    return "Reject"