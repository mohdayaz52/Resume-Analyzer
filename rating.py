def get_resume_rating(score):
    if score >= 90:
        return "★★★★★ Excellent"

    elif score >= 75:
        return "★★★★ Good"

    elif score >= 50:
        return "★★★ Average"

    elif score >= 25:
        return "★★ Needs Improvement"

    else:
        return "★ Poor"