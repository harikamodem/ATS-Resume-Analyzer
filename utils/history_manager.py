import pandas as pd
import os

def save_history(
    name,
    score,
    semantic,
    rank
):

    file = "logs/analysis_log.csv"

    data = {

        "Candidate":[name],

        "ATS":[score],

        "Semantic":[semantic],

        "Rank":[rank]
    }

    df = pd.DataFrame(
        data
    )

    if os.path.exists(
        file
    ):

        df.to_csv(
            file,
            mode="a",
            header=False,
            index=False
        )

    else:

        df.to_csv(
            file,
            index=False
        )