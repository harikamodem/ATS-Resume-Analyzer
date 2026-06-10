def keyword_stuffing(
        keyword_counts):

    total = sum(
        keyword_counts.values()
    )

    if total > 50:
        return True

    return False