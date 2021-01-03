# -*- coding: utf-8 -*-

from .closets.POS import pos_tags, total_pos_tags
from .lemmatizers import verb, non_verb
from .tools.general_tools import valid_str_param, valid_word_param
from .tools.text_tools import parse_word, parse_pos, is_greek


def stem_word(word: str, pos: str) -> str:
    """
    :param: word: string, required
    - The word to stem
    :param: word (str): string, required
    - The POS of given word
    :return: str
    - The stemmed word
    """
    if not valid_str_param(word):
        raise TypeError(f'Invalid parameter: {word}. Given text have to be a string')

    if not valid_word_param(word):
        raise TypeError(f'Invalid parameter: {word}. Given text have to be a single word.')

    if not valid_str_param(pos):
        raise TypeError(f'Invalid parameter: {pos}. Given POS tag have to a string')

    if not is_greek(word):
        return word.strip()

    # parse the given word and POS
    word = parse_word(word)
    pos = parse_pos(pos)

    if pos not in total_pos_tags:
        raise ValueError('Given Part of Speech Tag is not valid!')

    # if given word is verb or modal verb
    if pos in pos_tags['verbs']['singular'] + pos_tags['verbs']['plural']:
        return verb.stem(word, pos)
    else:
        return non_verb.stem(word, pos)
