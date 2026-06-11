def impact_score(
    achievement_count
):

    if achievement_count >= 15:
        return 100

    elif achievement_count >= 10:
        return 85

    elif achievement_count >= 5:
        return 70

    elif achievement_count >= 2:
        return 50

    return 20