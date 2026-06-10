from utils.semantic_match import (
    semantic_match
)

resume = """
Python
Machine Learning
Deep Learning
TensorFlow
NLP
Data Analysis
"""

jd = """
Python
Machine Learning
Deep Learning
TensorFlow
NLP
Data Analysis
"""

print(
    semantic_match(
        resume,
        jd
    )
)