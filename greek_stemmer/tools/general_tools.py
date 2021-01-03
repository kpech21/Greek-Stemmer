# -*- coding: utf-8 -*-

from typing import Optional


def valid_str_param(param) -> bool:
    """
    :param param: string, required
    :return: bool
    - Asserts whether param is valid.
    """
    return isinstance(param, str)


def valid_word_param(param: Optional[str]) -> bool:
    """
    :param param: string, required
    :return: bool
    - Asserts whether param is valid.
    """
    try:
        return True if len(param.split()) < 2 else False

    except AttributeError:
        return False
