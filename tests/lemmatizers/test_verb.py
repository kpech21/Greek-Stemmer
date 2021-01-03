# -*- coding: utf-8 -*-

import pytest

from greek_stemmer.lemmatizers.verb import stem


class TestVerbStem:

    # rule-set 1: check irregular verbs
    verb_stem_ruleset1 = [
        ('', 'VB', ''),
        ('ΕΙΜΑΙ', 'VB', 'ΕΙ'),
        ('ΕΙΜΑΣΤΕ', 'VBS', 'ΕΙ'),
        ('ΠΩ', 'VB', 'Π'),
        ('ΖΕΙΤΕ', 'VBS', 'Ζ'),
        ('ΖΟΥΣΑΜΕ', 'VBDS', 'Ζ'),
        ('ΔΕΙ', 'VB', 'Δ')
    ]

    @pytest.mark.parametrize('word, pos, output', verb_stem_ruleset1)
    def test_verb_stem_with_ruleset1(self, word, pos, output):

        assert stem(word, pos) == output

    # rule-set 2:  ACTIVE VOICE, Singular - PASSIVE VOICE, Singular
    verb_stem_ruleset2 = [
        ('', 'VB', ''),
        ('ΠΑΙΖΕΙ', 'VB', 'ΠΑΙΖ'),
        ('ΤΡΟΦΟΔΟΤΟΥΜΑΙ', 'VB', 'ΤΡΟΦΟΔΟΤ'),
        ('ΒΙΑΖΟΣΟΥΝΑ', 'VBD', 'ΒΙΑΖ'),
        ('ΔΙΑΣΚΕΔΑΖΑ', 'VBD', 'ΔΙΑΣΚΕΔΑΖ'),
        ('ΤΡΟΦΟΔΟΤΕΙ', 'VBF', 'ΤΡΟΦΟΔΟΤ'),
        ('ΕΧΩ', 'MD', 'ΕΧ')
    ]

    @pytest.mark.parametrize('word, pos, output', verb_stem_ruleset2)
    def test_verb_stem_with_ruleset2(self, word, pos, output):

        assert stem(word, pos) == output

    # rule-set 3: ACTIVE VOICE, Plural - PASSIVE VOICE, Plural
    verb_stem_ruleset3 = [
        ('', 'VBS', ''),
        ('ΑΠΟΤΕΛΕΙΣΤΕ', 'VBS', 'ΑΠΟΤΕΛ'),
        ('ΔΕΙΤΕ', 'VBS', 'Δ'),
        ('ΠΕΡΙΠΟΙΟΝΤΟΥΣΑΝ', 'VBDS', 'ΠΕΡΙΠΟ'),
        ('ΠΑΙΖΑΝ', 'VBDS', 'ΠΑΙΖ'),
        ('ΤΡΟΦΟΔΟΤΟΥΝ', 'VBFS', 'ΤΡΟΦΟΔΟΤ'),
        ('ΟΙΚΕΙΟΠΟΙΟΥΝΤΑΙ', 'VBS', 'ΟΙΚΕΙΟΠΟΙΟΥ')
    ]

    @pytest.mark.parametrize('word, pos, output', verb_stem_ruleset3)
    def test_verb_stem_with_various_ruleset3(self, word, pos, output):

        assert stem(word, pos) == output
