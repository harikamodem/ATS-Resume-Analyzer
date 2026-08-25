from utils.keyword_analyzer import (
    keyword_count
)

text = """
python python sql
docker python
"""

skills = [
    "python",
    "sql",
    "docker"
]

print(
    keyword_count(
        text,
        skills
    )
)