def quality_check(words):
    if words < 250:
        return "Resume is too short."
    elif words > 1000:
        return "Resume is too long."
    else:
        return "Resume length is good."