text = "python sql ml"
skill_list = ['python', 'sql', 'docker']
def extract_skills(text, skill_list):
    found_skills = []
    for skill in skill_list:
        if skill in text:
            found_skills.append(skill)
    return found_skills
print(extract_skills(text, skill_list))
