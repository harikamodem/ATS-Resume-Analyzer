def detect_projects(text):

    keywords = [
        "project",
        "developed",
        "built",
        "designed",
        "implemented",
        "created"
    ]

    count = 0

    text = text.lower()

    for word in keywords:

        count += text.count(
            word
        )

    return count