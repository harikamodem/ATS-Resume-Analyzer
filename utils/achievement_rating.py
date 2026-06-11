def achievement_rating(
    score
):

    if score >= 85:
        return "Excellent Achievement Profile"

    elif score >= 70:
        return "Strong Achievement Profile"

    elif score >= 50:
        return "Average Achievement Profile"

    return "Weak Achievement Profile"