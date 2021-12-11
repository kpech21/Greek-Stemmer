from typing import Any, Optional


def valid_str_param(param: Any) -> bool:
    """Method checks whether a given param is string

    Args:
        param (Any): A given param

    Returns:
        bool: Asserts whether param is string.
    """
    return isinstance(param, str)


def valid_word_param(param: Optional[str]) -> bool:
    """Method checks whether a given param is a word

    Args:
        param (str): A given string param

    Returns:
        bool: Asserts whether the given param is a single word.
    """
    try:
        return True if len(param.split()) < 2 else False

    except AttributeError:
        return False
