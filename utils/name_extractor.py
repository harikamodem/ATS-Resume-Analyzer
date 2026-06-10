def extract_name(text):

    lines = text.split("\n")

    if len(lines) > 0:
        return lines[0]

    return "Candidate"