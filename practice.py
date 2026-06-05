#Strings

resume = "Experienced Machine Learning Engineer"
print(resume.lower())
print(resume.upper())
print(len(resume))
print("Machine" in resume)
if "Machine Learning" in resume:
    print("Skill found")
print(resume.count("Machine Learning"))

text = "      Python, SQL, Machine Learning, HTML, CSS, Java"
print(text.lower())
print(text.split())
print(text.replace(",", ""))
print(text.strip())
text = text.lower()
text = text.replace(",", "")
text = text.strip()
print(text)

resume_skill = "PYTHON"
jd_skill = "python"
print(resume_skill.lower() == jd_skill)


#Lists

skills = ["Python", "SQL", "HTML"]
print(skills)
print(skills[0])
print(len(skills))
skills.append("Pandas")
skills.remove("HTML")
print(skills)
print("HTML" in skills)
required_skill = "SQL"
if required_skill in skills:
    print("Skill found")
for skill in skills:
    print(skill)
jd_skills = ["Python", "SQL", "Docker"]
#matched skills
for skill in jd_skills:
    if skill in skills:
        print(skill)
#missing skills
missing_skills = []
for skill in jd_skills:
    if skill not in skills:
        missing_skills.append(skill)
        print(missing_skills)
#string to list
skills = text.split()
print(skills)


#dictionaries

candidate = {
    "name": "Harika",
    "score": "70",
    "college": "IITK",
    "skills": ["Python", "SQL", "Pandas"],
    "analysis": {
        "matched_skills": [
            "Python"
        ]
    }
    }
print(candidate["score"])
#add
candidate["age"] = 20
#update
candidate["score"] = 85
print(candidate)
print(candidate["skills"])
print(candidate["skills"][0])
print("department" in candidate)
print(candidate.keys())
print(candidate.values())
for key, value in candidate.items():
    print(key, value)
print(candidate["analysis"]["matched_skills"])


#function

#function with input
def greet(name):
    print("Hi", name)
greet("Harika")
#returning values
def square(x):
    return x*x
result = square(11)
print(result)