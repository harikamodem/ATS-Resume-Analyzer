def keyword_count(
        text,
        skills):
    counts = {}
    for skill in skills:
        counts[skill] = text.count(skill)
    return counts