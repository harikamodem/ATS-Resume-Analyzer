import re

def detect_achievements(text):

    patterns = [

        r"\d+%",
        r"\d+\+",
        r"increased",
        r"improved",
        r"reduced",
        r"optimized",
        r"saved",
        r"generated",
        r"boosted",
        r"achieved",
        r"delivered",
        r"implemented"
    ]

    count = 0

    text = text.lower()

    for pattern in patterns:

        matches = re.findall(
            pattern,
            text
        )

        count += len(matches)

    return count