from utils.text_cleaner import clean_text
resume = "PYTHON, SQL & MACHINE LEARNING!!!"
cleaned = clean_text(resume)
print(cleaned)


from utils.text_cleaner import clean_text
samples = [
    "Experienced Python Developer",
    "SQL, Python & Machine Learning!",
    "Data Analyst     with SQL"
]
for text in samples:
    print(clean_text(text))