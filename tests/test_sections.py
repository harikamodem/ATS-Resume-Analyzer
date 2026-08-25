from utils.section_detector import (
    detect_sections
)
text = """

Education

Projects

Skills

"""

print(
    detect_sections(text)
)