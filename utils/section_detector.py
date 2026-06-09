def detect_sections(text):
    text = text.lower()
    sections = {
        "Education":
        "education" in text,

        "Experience":
        (
            "experience" in text
            or
            "internship" in text
        ),

        "Projects":
        "project" in text,

        "Skills":
        "skills" in text,

        "Certifications":
        (
            "certification" in text
            or
            "certifications" in text
        ),

        "Achievements":
        (
            "achievement" in text
            or
            "achievements" in text
        )
    }
    return sections