import os

from utils.resume_pipeline import (
    resume_pipeline
)

from utils.candidate_scoring import (
    candidate_scoring
)

def batch_processor(
    resumes,
    jd_text,
    skill_db,
    parser
):

    candidates = []

    for resume in resumes:

        temp_path = os.path.join(
            "uploads",
            resume.name
        )

        with open(
            temp_path,
            "wb"
        ) as f:

            f.write(
                resume.getbuffer()
            )

        text = parser(
            temp_path
        )

        ats, semantic = (
            resume_pipeline(
                text,
                jd_text,
                skill_db
            )
        )

        final_score = (
            candidate_scoring(
                ats,
                semantic
            )
        )

        candidates.append(
            {
                "name": resume.name,
                "ats": ats,
                "semantic": semantic,
                "score": final_score
            }
        )

    return candidates