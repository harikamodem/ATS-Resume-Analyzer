def cgpa_rating(cgpa):

    if cgpa is None:
        return "Not Found"

    if cgpa >= 9:
        return "Outstanding"

    elif cgpa >= 8:
        return "Excellent"

    elif cgpa >= 7:
        return "Good"

    else:
        return "Average"