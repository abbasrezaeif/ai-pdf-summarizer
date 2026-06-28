def create_basic_summary(text, max_characters=3000):
    if not text:
        return "No text available for summary."

    summary = text[:max_characters]

    return summary