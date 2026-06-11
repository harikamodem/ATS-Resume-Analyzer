def candidate_comparator(
    candidates
):

    return sorted(
        candidates,
        key=lambda x: x["rank"],
        reverse=True
    )