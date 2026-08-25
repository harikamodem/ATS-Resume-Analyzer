from utils.weighted_scorer import (
    weighted_score
)

resume = {
    "python",
    "sql"
}

jd = {
    "python",
    "sql",
    "docker",
    "git"
}

score = weighted_score(
    resume,
    jd
)

print(score)