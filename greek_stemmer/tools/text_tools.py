import unicodedata
from typing import Optional

# the greek alphabet
ALPHABET = frozenset('ΑΆΒΓΔΕΈΖΗΉΘΙΊΪΚΛΜΝΞΟΌΠΡΣΤΥΎΫΦΧΨΩΏαάβγδεέζηήθιίϊκλμνξοόπρστυύϋφχψωώς')


def parse_word(word: Optional[str]) -> str:
    """Method parses a given word.

    Args:
        word (str): A given string word.

    Returns:
        str: Return the parsed word.
    """
    if word is None:
        return ''

    # remove accents
    word = ''.join(c for c in unicodedata.normalize('NFD', word) if unicodedata.category(c) != 'Mn')

    # strip and convert to uppercase
    word = word.strip().upper()

    return word


def parse_pos(pos: Optional[str]) -> str:
    """Method parses a given POS.

    Args:
        pos (str): A given Part of Speech.

    Returns:
        str: Return the parsed Part of Speech.
    """
    if isinstance(pos, str):
        return pos.strip().upper()
    else:
        raise TypeError('POS tags are required to be string')


def is_greek(word: Optional[str]) -> bool:
    """Method checks whether a given word is greek.

    Args:
        word (Any): A given word.

    Returns:
        bool: Asserts whether word is greek.
    """
    if isinstance(word, str):
        return all(n in ALPHABET for n in word.strip())
    else:
        return False
