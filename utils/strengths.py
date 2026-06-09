def strongest_skills(
        keyword_counts):
    sorted_skills = sorted(
        keyword_counts.items(),
        key=lambda x: x[1],
        reverse=True
    )
    return sorted_skills[:5]