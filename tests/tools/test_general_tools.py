from greek_stemmer.tools.general_tools import *


class TestValidStrParam:

    def test_valid_str_param_none_param(self) -> None:

        assert not valid_str_param(param=None)

    def test_valid_str_param_str_param(self) -> None:

        assert valid_str_param(param=' ')

    def test_valid_str_param_int_param(self) -> None:

        assert not valid_str_param(param=1)

    def test_valid_str_param_list_param(self) -> None:

        assert not valid_str_param(param=[])

    def test_valid_str_param_tuple_param(self) -> None:

        assert not valid_str_param(param=())


class TestValidWordParam:

    def test_valid_word_param_none_param(self) -> None:

        assert not valid_word_param(param=None)

    def test_valid_word_param(self) -> None:

        assert valid_word_param(param='ελληνική')

    def test_valid_word_param_spaces(self) -> None:

        assert valid_word_param(param=' ελληνική ')

    def test_valid_word_param_eng_param(self) -> None:

        assert valid_word_param(param='greek')

    def test_valid_word_param_text_param(self) -> None:

        assert not valid_word_param(param='ελληνική σύνταξη ')
