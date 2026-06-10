def detect_experience(
        text):

    keywords = [
        "intern",
        "internship",
        "research",
        "work experience",
        "training"
    ]

    text = text.lower()

    count = 0

    for word in keywords:
        count += text.count(
            word
        )

    return count