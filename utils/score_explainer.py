def explain_score(
        score):

    if score >= 90:
        return "Excellent alignment with job requirements."

    elif score >= 70:
        return "Strong match with some gaps."

    elif score >= 50:
        return "Moderate match."

    else:
        return "Significant skill gaps detected."