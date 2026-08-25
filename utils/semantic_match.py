from utils.model_cache import (
    load_model
)
from sklearn.metrics.pairwise import (
    cosine_similarity
)

model = load_model()

def semantic_match(
        resume_text,
        jd_text):

    resume_embedding = model.encode(
        [resume_text]
    )

    jd_embedding = model.encode(
        [jd_text]
    )

    similarity = cosine_similarity(
        resume_embedding,
        jd_embedding
    )[0][0]

    return round(
        similarity * 100,
        2
    )