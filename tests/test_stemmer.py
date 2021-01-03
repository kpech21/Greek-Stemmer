# -*- coding: utf-8 -*-

import pytest

from greem_stemmer.stemmer import stem_word


class TestStemWord:

    def test_stem_word_raises_type_error(self):

        with pytest.raises(TypeError):
            stem_word(word=None, pos='NNM')

        with pytest.raises(TypeError):
            stem_word(word='εργαζόμενος', pos=None)

        with pytest.raises(ValueError):
            stem_word(word='εργαζόμενος', pos='XXXX')

        with pytest.raises(TypeError):
            stem_word(word='Ολόκληρη πρόταση', pos='JJM')

    stem_word_testdata = [
        ('English', 'NNPSN', 'English'),
        (' ΕλληνικάR ', 'NNPSN', 'ΕλληνικάR'),
        ('', 'PRP', ''),
        (' τραπέζι', 'NNN', 'ΤΡΑΠΕΖ'),
        ('γκαζόν', 'NNN', 'ΓΚΑΖΟΝ'),
        (' ενός ', 'DDT', 'ΕΝΟΣ'),
        ('ιδιαίτερες', 'JJSF', 'ΙΔΙΑΙΤΕΡ'),
        ('ποιός', 'WP', 'ΠΟΙ'),
        ('τροποποιεί ', 'VB', 'ΤΡΟΠΟΠΟΙ'),
        ('ευτυχισμένος  ', 'VBP', 'ΕΥΤΥΧΙΣ'),
        ('ορμωμένη', 'VBPD', 'ΟΡΜ'),
        ('21/04/1989', 'DATE', '21/04/1989'),
        ('20:31', 'TIME', '20:31'),
        ('!!', 'AB', '!!'),
        ('($)', 'SYM', '($)')
    ]

    @pytest.mark.parametrize('word, pos, output', stem_word_testdata)
    def test_stem_word_with_testdata(self, word, pos, output):

        assert stem_word(word, pos) == output
