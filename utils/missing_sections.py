def missing_sections(
        sections):

    result = []

    for section, status in sections.items():

        if not status:
            result.append(
                section
            )

    return result