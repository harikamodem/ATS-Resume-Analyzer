from utils.project_detector import (
    detect_projects
)

text = """
Developed AI Resume Analyzer.
Built Chatbot using Python.
Created ATS System.
"""

print(
    detect_projects(text)
)