from plover.formatting import WORD_RX

def stitch_word(word, delimiter='-'):
    text = ''
    words = WORD_RX.findall(word)
    for w in words:
        sw = w.rstrip()
        text += delimiter.join(w.rstrip()) + w[len(sw):]
    return text

def alternate_case(word, invert=False):
    text = ''
    words = WORD_RX.findall(word)
    for w in words:
        sw = w.rstrip()
        chars = ''
        is_upper = invert
        for ch in sw:
            if ch.isalpha():
                chars += ch.upper() if is_upper else ch.lower()
                is_upper = not is_upper
            else:
                chars += ch
        text += chars + w[len(sw):]
    return text