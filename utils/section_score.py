def section_score(
        sections):

    total = len(
        sections
    )

    present = sum(
        sections.values()
    )

    return (
        present /
        total
    ) * 100