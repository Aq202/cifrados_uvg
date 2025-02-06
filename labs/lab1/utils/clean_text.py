def clean_text(text, allowed_chars):
    text = text.lower()
    return "".join(char for char in text if char in allowed_chars)