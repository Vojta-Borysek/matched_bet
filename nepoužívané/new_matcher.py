from difflib import SequenceMatcher


def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

print(similarity('inter - slavia praha', 'internazionale - slavia prague'))