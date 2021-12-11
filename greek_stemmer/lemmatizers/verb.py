from ..closets.POS import pos_tags
from ..closets.rules import rules

# the greek vowels
VOWELS = frozenset('ΑΕΗΙΟΥΩ')


def stem(word: str, pos: str) -> str:
    """Stem method responsible to apply lemmatization in a non-verb word

    Args:
        word (str): The word to stem.
        pos (str): The POS of the given word.

    Returns:
        str: Return the lemmatized word
    """
    # rule-set 1: Irregular verbs
    if word in rules['verbs']['irregular']['type_1']:
        return 'ΕΙ'
    elif word in rules['verbs']['irregular']['type_2']:
        return word[0]

    # rule-set 2: ACTIVE VOICE, Singular - PASSIVE VOICE, Singular
    if pos in pos_tags['verbs']['singular']:

        for suffix in rules['verbs']['singular']:

            # exception: if the last letter of stemmed word is vowel
            if suffix == 'ΙΟΤΑΝ' and len(word) > 5:
                if word[-6] in VOWELS:
                    continue

            if word.endswith(suffix):
                return word[:len(word) - len(suffix)]

    # rule-set 3: ACTIVE VOICE, Plural - PASSIVE VOICE, Plural
    else:

        for suffix in rules['verbs']['plural']:

            # exception: if the last letter of stemmed word is vowel
            if suffix in ['ΙΟΥΝΤΑΙ', 'ΙΟΥΝΤΑΝ'] and len(word) > 7:
                if word[-8] in VOWELS:
                    continue

            if word.endswith(suffix):
                return word[:len(word) - len(suffix)]

    return word
