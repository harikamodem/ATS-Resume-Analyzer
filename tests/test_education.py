from utils.education_detector import (
    detect_education
)

text = """
Education

B.Tech Mechanical Engineering
IIT Kanpur
"""

print(
    detect_education(text)
)