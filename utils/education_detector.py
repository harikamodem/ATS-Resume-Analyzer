def detect_education(text):

    text = text.lower()

    sections = [
        "education",
        "b.tech",
        "btech",
        "bachelor",
        "master",
        "m.tech",
        "iit",
        "university"
    ]

    found = []

    for item in sections:

        if item in text:
            found.append(item)

    return found