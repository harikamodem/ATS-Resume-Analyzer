def keyword_density(
    text,
    keyword
):

    total_words = len(
        text.split()
    )

    if total_words == 0:
        return 0

    count = text.lower().count(
        keyword.lower()
    )

    return round(
        (count / total_words) * 100,
        2
    )