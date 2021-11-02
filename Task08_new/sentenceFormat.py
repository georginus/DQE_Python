from Task04_refactor03.Refactor03 import formatText


def sentenceFormatted(text):
    sentence_formatted = '. '.join(map(lambda s: s.strip().capitalize(), formatText(text).split('.')))
    return sentence_formatted
