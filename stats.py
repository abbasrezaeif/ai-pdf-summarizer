def count_characters(text):
    return len(text)


def count_words(text):
    words = text.split()
    return len(words)


def estimate_reading_time(word_count, words_per_minute=200):
    minutes = word_count / words_per_minute

    if minutes < 1:
        return "Less than 1 minute"

    hours = int(minutes // 60)
    remaining_minutes = int(minutes % 60)

    if hours > 0:
        return f"{hours} hours {remaining_minutes} minutes"

    return f"{remaining_minutes} minutes"