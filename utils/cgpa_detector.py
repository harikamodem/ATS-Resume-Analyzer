import re

def detect_cgpa(text):

    match = re.search(
        r"\d\.\d\d",
        text
    )

    if match:
        return float(
            match.group()
        )

    return None