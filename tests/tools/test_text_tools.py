from typing import List, Tuple

import pytest

from greek_stemmer.tools.text_tools import *


class TestParseText:

    def test_parse_word_receives_no_string(self) -> None:

        assert parse_word(None) == ''

    # check accents removal and uppercase letters
    parse_word_testdata: List[Tuple] = [
        (' $', '$'),
        (' foo ', 'FOO'),
        ('(25%)', '(25%)'),
        (u'\u2167 ί', 'Ⅷ Ι'),
        ("Greek's", "GREEK'S"),
        ('κ', 'Κ'),
        ('ιστορικός', 'ΙΣΤΟΡΙΚΟΣ'),
        ('Ιστορικός ', 'ΙΣΤΟΡΙΚΟΣ'),
        ('ΙΣΤΟΡΙΚΌΣ', 'ΙΣΤΟΡΙΚΟΣ'),
        ('Λαϊκός', 'ΛΑΙΚΟΣ'),
        (' ΛΑΪΚΌΣ', 'ΛΑΙΚΟΣ')
    ]

    @pytest.mark.parametrize('word, output', parse_word_testdata)
    def test_parse_word_with_various_inputs(self, word: str, output: str) -> None:

        assert parse_word(word) == output


class TestParsePos:

    def test_parse_pos_receives_no_string(self) -> None:

        with pytest.raises(TypeError):
            parse_pos(None)

    # check accents removal and uppercase letters
    parse_pos_testdata: List[Tuple] = [
        (' $', '$'),
        (' foo ', 'FOO'),
        ('(25%)', '(25%)'),
        (u'\u2167 ι', 'Ⅷ Ι'),
        ("Greek's", "GREEK'S"),
        ('κ', 'Κ'),
        ('nnsf', 'NNSF'),
        ('vbfs ', 'VBFS'),
        (' prp', 'PRP'),
        ('Inp', 'INP'),
        (' date ', 'DATE')
    ]

    @pytest.mark.parametrize('word, output', parse_pos_testdata)
    def test_parse_pos_with_various_inputs(self, word: str, output: str) -> None:

        assert parse_pos(word) == output


class TestIsGreek:

    def test_is_greek_receives_no_string(self) -> None:

        assert is_greek(None) is False

    # check accents removal and uppercase letters
    parse_is_greek_testdata: List[Tuple] = [
        (' $', False),
        ('0.5', False),
        ('foo', False),
        ('(25%)', False),
        (u'\u2167 ί', False),
        ("Greek's", False),
        ('κ', True),
        ('eλληνικά', False),
        ('EΛΛΗΝΙΚΆ', False),
        ('ΕΛΛΗΝΙΚΑ', True),
        (' ελληνικά', True),
        ('NOT', False),
        ('ΝΟΤ', True),
        (' Λαϊκός ', True),
        ('ΛΑΪΚΌΣ', True)
    ]

    @pytest.mark.parametrize('word, output', parse_is_greek_testdata)
    def test_is_greek_with_various_inputs(self, word: str, output: str) -> None:

        assert is_greek(word) == output
