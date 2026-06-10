def benchmark_score(score):

    industry_average = 65

    if score > industry_average:

        return (
            "Above Industry Average",
            industry_average
        )

    return (
        "Below Industry Average",
        industry_average
    )