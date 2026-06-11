def shortlist_engine(
    candidates
):

    shortlisted = []

    for candidate in candidates:

        if candidate["rank"] >= 75:

            shortlisted.append(
                candidate
            )

    return shortlisted