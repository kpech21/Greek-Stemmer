# -*- coding: utf-8 -*-

import unicodedata
from typing import Optional

# the greek alphabet
ALPHABET = frozenset('ΑΆΒΓΔΕΈΖΗΉΘΙΊΪΚΛΜΝΞΟΌΠΡΣΤΥΎΫΦΧΨΩΏαάβγδεέζηήθιίϊκλμνξοόπρστυύϋφχψωώς')


def parse_word(word: Optional[str]) -> str:
    """
    :param: word: string, required
    :return: string
    """
    if word is None:
        return ''

    # remove accents
    word = ''.join(c for c in unicodedata.normalize('NFD', word) if unicodedata.category(c) != 'Mn')

    # strip and convert to uppercase
    word = word.strip().upper()

    return word


def parse_pos(pos: Optional[str]) -> str:
    """
    Parses of POS
    :param: pos: string, required
    :return: string
    """
    if isinstance(pos, str):
        return pos.strip().upper()
    else:
        raise TypeError('POS tags are required to be strings')


def is_greek(word: Optional[str]) -> bool:
    """
    Checks whether a word is greek or not.
    :param: word: str, required
    :return: bool
    """
    if isinstance(word, str):
        return all(n in ALPHABET for n in word.strip())
    else:
        return False
