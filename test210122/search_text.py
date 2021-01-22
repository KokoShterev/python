def search_and_replace_text(search_sentence, text):
    if search_sentence in text:
        text = text.replace(search_sentence, '')
        text += " sedem"
    return text