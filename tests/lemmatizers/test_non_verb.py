# -*- coding: utf-8 -*-

import pytest

from greem_stemmer.lemmatizers.non_verb import stem


class TestVerbStem:

    # rule-set 1Α: unlemmatized words
    # rule-set 1B: unlemmatized words
    # rule-set 1C: Numbers
    verb_stem_ruleset1abc = [
        ('', 'JJM', ''),
        ('ΤΩΝ', 'DDT', 'ΤΩΝ'),
        ('ΜΙΑ', 'IDT', 'ΜΙΑ'),
        ('ΚΟΒΙΝΤ', 'NNM', 'ΚΟΒΙΝΤ'),
        ('ΣΕΡΦΙΝΓΚ', 'NNN', 'ΣΕΡΦΙΝΓΚ'),
        ('ΕΞΩ', 'RB', 'ΕΞΩ'),
        ('ΕΙΚΟΣΙ', 'JJΝ', 'ΕΙΚΟΣΙ'),
        ('ΔΥΟ', 'JJn', 'ΔΥΟ')
    ]

    @pytest.mark.parametrize('word, pos, output', verb_stem_ruleset1abc)
    def test_verb_stem_with_ruleset1abc(self, word, pos, output):

        assert stem(word, pos) == output

    # rule-set 1D: ΕΝΔΟΝ, have always the lemma 'endon'
    verb_stem_ruleset1d = [
        ('', 'JJSM', ''),
        ('ΕΝΔΟΤΕΡΟΣ', 'JJSM', 'ΕΝΔΟΝ'),
        ('ΕΝΔΟΤΕΡΑ', 'JJSN', 'ΕΝΔΟΝ')
    ]

    @pytest.mark.parametrize('word, pos, output', verb_stem_ruleset1d)
    def test_verb_stem_with_ruleset1d(self, word, pos, output):

        assert stem(word, pos) == output

    # rule-set 1e: ΠΛΗΣΙΟΝ, have always the lemma 'plision'
    verb_stem_ruleset1e = [
        ('', 'JJSM', ''),
        ('ΠΛΗΣΙΕΣΤΕΡΗ', 'JJF', 'ΠΛΗΣΙΟΝ'),
        ('ΠΛΗΣΙΕΣΤΕΡΕΣ', 'JJSF', 'ΠΛΗΣΙΟΝ')
    ]

    @pytest.mark.parametrize('word, pos, output', verb_stem_ruleset1e)
    def test_verb_stem_with_ruleset1e(self, word, pos, output):

        assert stem(word, pos) == output

    # rule-set 1F: ΠΡΟΤΙΜΩ, have always the lemma 'protimo'
    verb_stem_ruleset1f = [
        ('', 'JJSM', ''),
        ('ΠΡΟΤΙΜΟΤΕΡΟΣ', 'JJM', 'ΠΡΟΤΙΜΩ'),
        ('ΠΡΟΤΙΜΟΤΕΡΟΥ', 'JJSM', 'ΠΡΟΤΙΜΩ')
    ]

    @pytest.mark.parametrize('word, pos, output', verb_stem_ruleset1f)
    def test_verb_stem_with_ruleset1f(self, word, pos, output):

        assert stem(word, pos) == output

    # rule-set 1G: noun with extra sigma
    verb_stem_ruleset1g = [
        ('', 'NNN', ''),
        ('ΠΕΡΑΣ', 'NNN', 'ΠΕΡΑ'),
        ('ΗΜΙΦΩΣ', 'NNN', 'ΗΜΙΦΩ')
    ]

    @pytest.mark.parametrize('word, pos, output', verb_stem_ruleset1g)
    def test_verb_stem_with_ruleset1g(self, word, pos, output):

        assert stem(word, pos) == output

    # rule-set 2: neuter noun with suffix ΜΑΤΟΣ, ΜΑΤΑ, ΜΑΤΩΝ, ΜΑ
    verb_stem_ruleset2 = [
        ('', 'VBS', ''),
        ('ΧΑΡΑΜΑΤΑ', 'NNSN', 'ΧΑΡΑΜ'),
        ('ΧΡΩΜΑΤΩΝ', 'NNSN', 'ΧΡΩΜ')
    ]

    @pytest.mark.parametrize('word, pos, output', verb_stem_ruleset2)
    def test_verb_stem_with_various_ruleset2(self, word, pos, output):

        assert stem(word, pos) == output

    # rule-set 3: suffix for proper names
    verb_stem_ruleset3 = [
        ('', 'NNPN', ''),
        ('ΑΝΑΣΤΑΣΕΩΣ', 'NNPF', 'ΑΝΑΣΤΑΣ'),
        ('ΒΩΛΑΞ', 'NNPM', 'ΒΩΛΑ')
    ]

    @pytest.mark.parametrize('word, pos, output', verb_stem_ruleset3)
    def test_verb_stem_with_various_ruleset3(self, word, pos, output):

        assert stem(word, pos) == output

    # rule-set 4: irregular adjectives
    verb_stem_ruleset4 = [
        ('', 'JJM', ''),
        ('ΑΝΩΤΕΡΟΥΣ', 'JJSM', 'ΑΝΩ'),
        ('ΚΑΤΩΤΑΤΟΙ', 'JJSM', 'ΚΑΤΩ'),
        ('ΥΠΕΡΤΑΤΑ', 'JJSN', 'ΥΠΕΡ'),
        ('ΑΠΩΤΕΡΟ', 'JJN', 'ΑΠΩ')
    ]

    @pytest.mark.parametrize('word, pos, output', verb_stem_ruleset4)
    def test_verb_stem_with_various_ruleset4(self, word, pos, output):

        assert stem(word, pos) == output

    # rule-set 5: Adjectives, Participles and Pronouns
    verb_stem_ruleset5 = [
        ('', 'JJSN', ''),
        ('ΕΝΑ', 'CD', 'ΕΝ'),
        ('ΔΕΚΑΤΕΣΣΕΡΑ', 'CD', 'ΔΕΚΑΤΕΣΣΕΡ'),
        ('ΕΜΕΝΑ', 'PRP', 'Ε'),
        ('ΟΠΟΙΑ', 'WP', 'ΟΠΟΙ'),
        ('ΙΔΙΟ', 'DP', 'ΙΔΙ'),
        ('ΚΑΠΟΙΟΙ', 'INP', 'ΚΑΠΟΙ'),
        ('ΟΜΟΡΦΗ', 'JJF', 'ΟΜΟΡΦ'),
        ('ΑΠΛΟΥΣΤΕΡΟΣ', 'JJM', 'ΑΠΛ'),
        ('ΗΤΤΗΜΕΝΟΙ', 'JJSM', 'ΗΤΤ'),
        ('ΤΡΑΝΟ', 'JJN', 'ΤΡΑΝ'),
        ('ΕΡΓΑΖΟΜΕΝΟΣ', 'VBG', 'ΕΡΓΑΖ'),
        ('ΝΙΚΗΜΕΝΗΣ', 'VBG', 'ΝΙΚ')
    ]

    @pytest.mark.parametrize('word, pos, output', verb_stem_ruleset5)
    def test_verb_stem_with_various_ruleset5(self, word, pos, output):

        assert stem(word, pos) == output

    # rule-set 6: Singular Noun
    verb_stem_ruleset6 = [
        ('', 'NNPN', ''),
        ('ΔΡΟΜΕΑΣ', 'NNF', 'ΔΡΟΜΕ'),
        ('ΟΛΥΜΠΙΑΣ', 'NNPF', 'ΟΛΥΜΠΙ'),
        ('ΚΑΙΡΟΥΣ', 'NNM', 'ΚΑΙΡ'),
        ('ΠΕΙΘΩ', 'NNF', 'ΠΕΙΘ')
    ]

    @pytest.mark.parametrize('word, pos, output', verb_stem_ruleset6)
    def test_verb_stem_with_various_ruleset6(self, word, pos, output):

        assert stem(word, pos) == output

    # rule-set 7: Plural Noun
    verb_stem_ruleset7 = [
        ('', 'NNPSN', ''),
        ('ΠΑΡΑΔΕΙΣΩΝ', 'NNSF', 'ΠΑΡΑΔ'),
        ('ΔΑΣΗ', 'NNSN', 'ΔΑΣ'),
        ('ΑΔΡΙΑΤΙΚΟΥΣ', 'NNPSM', 'ΑΔΡΙΑΤΙΚ'),
        ('ΙΟΝΙΩΝ', 'NNPSN', 'ΙΟΝΙ')
    ]

    @pytest.mark.parametrize('word, pos, output', verb_stem_ruleset7)
    def test_verb_stem_with_various_ruleset7(self, word, pos, output):

        assert stem(word, pos) == output

    # rule-set 8: Adverb
    verb_stem_ruleset8 = [
        ('', 'RB', ''),
        ('ΑΠΛΟΥΣΤΑΤΑ', 'RB', 'ΑΠΛ'),
        ('ΒΑΡΥΤΑΤΑ', 'RB', 'ΒΑΡ'),
        ('ΔΙΑΡΚΩΣ', 'RB', 'ΔΙΑΡΚ'),
        ('ΑΥΡΙΟ', 'RB', 'ΑΥΡΙ')
    ]

    @pytest.mark.parametrize('word, pos, output', verb_stem_ruleset8)
    def test_verb_stem_with_various_ruleset8(self, word, pos, output):

        assert stem(word, pos) == output
