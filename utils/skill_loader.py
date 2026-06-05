def load_skills(path):
    with open(path, "r") as file:
        skills = [
            skill.strip()
            for skill in file
        ]
    return skills