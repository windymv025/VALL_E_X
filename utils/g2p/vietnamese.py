from viphoneme import vi2IPA


def vietnamese_to_ipa(text):
    text = vi2IPA(text)
    return text.replace('...', '…')
