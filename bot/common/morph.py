import pymorphy2
morph = pymorphy2.MorphAnalyzer()


def get_morph(text, count):
    text_morph = morph.parse(text)[0]
    text_morph.inflect({'gent'})
    return text_morph.make_agree_with_number(count).word