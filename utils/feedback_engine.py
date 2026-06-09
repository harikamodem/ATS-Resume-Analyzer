def generate_feedback(
        score):
    if score >= 80:
        return (
            "Excellent ATS compatibility."
        )
    elif score >= 60:
        return (
            "Good match. Add a few more skills."
        )
    elif score >= 40:
        return (
            "Average match. Resume needs improvement."
        )
    else:
        return (
            "Low ATS score. Consider tailoring your resume."
        )