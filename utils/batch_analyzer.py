from utils.resume_ranker import (
    resume_ranker
)

def batch_analyzer(
    candidates
):

    results = []

    for candidate in candidates:

        rank = resume_ranker(
            candidate["ats"],
            candidate["semantic"],
            candidate["career"],
            candidate["education"]
        )

        candidate["rank"] = rank

        results.append(
            candidate
        )

    return results