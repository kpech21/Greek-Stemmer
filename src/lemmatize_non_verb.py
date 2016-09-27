# -*- coding: utf-8 -*-
# !/usr/bin/python
#   stemmer_gr.py is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   stemmer_gr.py is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with Foobar.  If not, see <http://www.gnu.org/licenses/>.

#########################################################################################################################################
#       THESIS	: Corpus Based Methods for Learning Models of Metaphor in Modern Greek	                                                #
#                                                                                                                                       #
#       AUTHOR	: Konstantinos Pechlivanis                                                                                              #
#                                                                                                                                       #
#       SUMMARY : this function finds the lemma of words (except for verbs), function "stem" estimates the lemma                        #
#                 and function "ends_with" estimates the suffix                                                                         #
#                                                                                                                                       #
#       OUTPUTS	: return the lemma of word                                                                                              #
#########################################################################################################################################


def ends_with(word, suffix):
    """
    :param word: string, required
    :param suffix: string, required
    :return: bool
        -Return True if the word ends with the specific suffix, othrewise, return False
    """
    return word[len(word) - len(suffix):] == suffix


def stem(word, pos, is_unlemmatized_word, has_extra_sigma, irregular_adjectives, has_lemma_endon, has_lemma_plision, has_lemma_protimo, numbers):
    """
    :param word: string, required
    :param pos: string, required
    :param is_unlemmatized_word: list, required
    :param has_extra_sigma: list, required
    :param irregular_adjectives: list, required
    :param has_lemma_endon: list, required
    :param has_lemma_plision: list, required
    :param has_lemma_protimo: list, required
    :param numbers: list, required
    :return: string
        -Return the lemmatized word
    """
    # rule-set 1Α ---> for the unlemmatized words, initial and lemmatized words are same
    if word in is_unlemmatized_word:
        return word

    # rule-set 1Β ---> ΕΝΔΟΝ, greek words have always the lemma "endon"
    elif word in has_lemma_endon:
        return 'ΕΝΔΟΝ'

    # rule-set 1C ---> ΠΛΗΣΙΟΝ, greek words have always the lemma "plision"
    elif word in has_lemma_plision:
        return 'ΠΛΗΣΙΟΝ'

    # rule-set 1D ---> ΠΡΟΤΙΜΩ, greek words have always the lemma "protimo"
    elif word in has_lemma_protimo:
        return 'ΠΡΟΤΙΜΩ'

    # rule-set 1E ---> Numbers, same as rule-set 1A
    elif word in numbers:
        return word

    # rule-set 1F ---> noun with extra sigma
    elif word in has_extra_sigma:
        return word[:-1]

    # rule-set 2 ---> neuter noun with suffix ΜΑΤΟΣ, ΜΑΤΑ, ΜΑΤΩΝ, ΜΑ
    if pos in ['NNN', 'NNSN', 'NNPN', 'NNPSN']:
        for suffix in [u'ΜΑΤΟΣ', u'ΜΑΤΩΝ', u'ΜΑΤΑ', u'ΜΑ']:
            if ends_with(word, suffix):
                return word[:len(word) - len(suffix)] + u'Μ'     # reduce the suffix and add M character

    # rule-set 3 ---> suffix for proper names
    if pos in ['NNPM', 'NNPF', 'NNPN', 'NNPSM', 'NNPSF', 'NNPSN']:
        suffix = [u'ΟΝΟΣ', u'ΩΝΟΣ', u'ΟΡΟΣ', u'ΕΥΣ', u'ΕΩΣ', u'ΟΝΤΟΣ', u'ΚΤΟΣ', u'ΟΥΣ', u'ΩΝ', u'ΩΡ', u'ΙΣ', u'ΩΣ', u'Ξ', u'Ω']
        for ii in range(len(suffix)):
            if ends_with(word, suffix[ii]):
                return word[:len(word) - len(suffix[ii])]

    # rule-set 4 ---> Adjectives AND Participles
    if 'JJ' in pos or pos in ['VBG', 'VBP', 'VBPD', 'PRP', 'PP', 'REP', 'DP', 'IP', 'WP', 'QP', 'INP', 'CD']:
        suffix = [u'ΟΥΣΤΕΡΟΥΣ', u'ΟΥΣΤΑΤΟΥΣ', u'ΟΥΣΤΕΡΟΥ', u'ΟΥΣΤΕΡΟΣ', u'ΕΣΤΕΡΟΥΣ', u'ΟΥΣΤΕΡΗΣ', u'ΕΣΤΑΤΟΥΣ', u'ΟΥΣΤΕΡΩΝ', u'ΟΥΣΤΑΤΕΣ', u'ΟΥΣΤΕΡΕΣ',
                  u'ΟΥΣΤΕΡΟΙ', u'ΑΙΤΕΡΟΥΣ', u'ΟΥΣΤΑΤΟΣ', u'ΟΥΣΤΑΤΟΥ', u'ΟΥΣΤΑΤΗΣ', u'ΟΥΣΤΑΤΩΝ', u'ΥΤΕΡΟΥΣ', u'ΕΣΤΕΡΟΙ', u'ΕΣΤΕΡΩΝ', u'ΕΣΤΕΡΕΣ',
                  u'ΟΥΣΤΕΡΗ', u'ΩΜΕΝΟΥΣ', u'ΕΣΤΑΤΗΣ', u'ΕΣΤΕΡΑΣ', u'ΕΣΤΕΡΗΣ', u'ΟΥΣΤΕΡΟ', u'ΑΣΜΕΝΟΙ', u'ΟΤΕΡΟΥΣ', u'ΕΣΤΑΤΟΥ', u'ΕΣΤΑΤΟΣ', u'ΟΥΣΤΕΡΑ',
                  u'ΕΣΤΑΤΕΣ', u'ΥΤΑΤΟΥΣ', u'ΕΣΤΕΡΟΥ', u'ΕΣΤΕΡΟΣ', u'ΑΙΤΕΡΟΣ', u'ΑΙΤΕΡΟΥ', u'ΕΣΤΑΤΟΙ', u'ΑΙΤΕΡΟΙ', u'ΑΙΤΕΡΩΝ', u'ΑΙΤΕΡΗΣ', u'ΑΙΤΕΡΑΣ',
                  u'ΟΥΜΕΝΟΥ', u'ΟΥΜΕΝΟΣ', u'ΟΥΜΕΝΗΣ', u'ΟΥΜΕΝΩΝ', u'ΟΥΜΕΝΕΣ', u'ΟΜΕΝΟΥΣ', u'ΕΣΤΑΤΩΝ', u'ΕΣΤΕΡΟΝ', u'ΗΜΕΝΟΥΣ', u'ΟΥΣΤΑΤΗ', u'ΟΥΣΤΑΤΑ',
                  u'ΕΣΤΕΡΟΝ', u'ΟΥΣΤΑΤΟ', u'ΩΤΕΡΟΥΣ', u'ΩΤΑΤΟΥΣ', u'ΥΤΕΡΕΣ', u'ΩΜΕΝΟΥ', u'ΟΤΑΤΩΝ', u'ΕΣΤΑΤΟ', u'ΕΣΤΑΤΗ', u'ΥΤΑΤΩΝ', u'ΥΤΕΡΗΣ',
                  u'ΟΜΕΝΟΣ', u'ΟΤΕΡΟΙ', u'ΟΤΕΡΩΝ', u'ΥΤΑΤΟΣ', u'ΥΤΑΤΟΥ', u'ΕΣΤΑΤΑ', u'ΥΤΑΤΗΣ', u'ΟΤΕΡΟΣ', u'ΟΤΕΡΟΥ', u'ΥΤΑΤΕΣ', u'ΟΤΕΡΕΣ', u'ΥΤΕΡΟΙ',
                  u'ΥΤΕΡΩΝ', u'ΑΙΤΕΡΟ', u'ΟΤΕΡΗΣ', u'ΥΤΕΡΟΣ', u'ΑΙΤΕΡΗ', u'ΑΙΤΕΡΑ', u'ΜΕΝΟΥΣ', u'ΥΤΕΡΟΥ', u'ΩΜΕΝΗΣ', u'ΩΜΕΝΩΝ', u'ΩΜΕΝΕΣ', u'ΟΥΜΕΝΟ',
                  u'ΟΥΜΕΝΗ', u'ΟΥΜΕΝΑ', u'ΟΜΕΝΕΣ', u'ΩΜΕΝΟΣ', u'ΟΜΕΝΗΣ', u'ΟΜΕΝΩΝ', u'ΕΣΤΕΡΟ', u'ΕΣΤΕΡΗ', u'ΕΣΤΕΡΑ', u'ΟΤΑΤΟΣ', u'ΟΤΑΤΗΣ', u'ΟΜΕΝΟΥ',
                  u'ΟΤΑΤΟΙ', u'ΥΤΑΤΟΙ', u'ΟΤΑΤΟΥ', u'ΗΜΕΝΗΣ', u'ΟΜΕΝΟΙ', u'ΗΜΕΝΟΥ', u'ΗΜΕΝΟΙ', u'ΗΜΕΝΩΝ', u'ΜΕΝΟΥΣ', u'ΗΜΕΝΟΣ', u'ΩΜΕΝΟΙ', u'ΟΤΑΤΕΣ',
                  u'ΩΤΕΡΟΣ', u'ΩΤΕΡΟΥ', u'ΩΤΕΡΟΝ', u'ΩΤΕΡΟΙ', u'ΩΤΕΡΩΝ', u'ΩΤΕΡΗΣ', u'ΩΤΕΡΕΣ', u'ΩΤΕΡΑΣ', u'ΩΤΑΤΟΣ', u'ΩΤΑΤΟΥ', u'ΩΤΑΤΟΙ', u'ΩΤΑΤΩΝ',
                  u'ΩΤΑΤΗΣ', u'ΩΤΑΤΕΣ', u'ΜΕΝΟΣ', u'ΜΕΝΟΥ', u'ΜΕΝΗΣ', u'ΜΕΝΟΙ', u'ΜΕΝΩΝ', u'ΩΜΕΝΟ', u'ΩΜΕΝΗ', u'ΩΜΕΝΑ', u'ΥΤΕΡΑ', u'ΥΤΑΤΑ', u'ΥΤΕΡΟ',
                  u'ΟΤΑΤΗ',  u'ΜΕΝΕΣ', u'ΟΜΕΝΑ', u'ΩΜΕΝΟ', u'ΩΜΕΝΗ', u'ΟΤΕΡΟ', u'ΟΤΕΡΗ', u'ΕΙΣΕΣ', u'ΟΜΕΝΟ', u'ΟΜΕΝΗ', u'ΥΤΕΡΗ', u'ΟΤΕΡΑ', u'ΜΕΝΟΙ',
                  u'ΥΤΑΤΗ', u'ΟΤΑΤΟ', u'ΟΤΑΤΑ', u'ΜΕΝΟΥ', u'ΜΕΝΟΣ', u'ΗΜΕΝΗ', u'ΜΕΝΩΝ', u'ΜΕΝΗΣ', u'ΗΜΕΝΟ', u'ΗΜΕΝΑ', u'ΟΝΤΑΣ', u'ΩΝΤΑΣ', u'ΩΤΕΡΟ',
                  u'ΩΤΕΡΕ', u'ΩΤΕΡΗ', u'ΩΤΕΡΑ', u'ΩΤΑΤΟ', u'ΩΤΑΤΕ', u'ΩΤΑΤΗ', u'ΩΤΑΤΑ', u'ΜΕΝΟ', u'ΜΕΝΗ', u'ΜΕΝΑ', u'ΕΙΕΣ', u'ΕΙΩΝ', u'ΟΥΣ', u'ΕΩΣ',
                  u'ΕΟΣ', u'ΩΣΑ', u'ΟΥΝ', u'ΕΙΣ', u'ΟΥΣ', u'ΕΩΝ', u'ΙΣ', u'ΟΣ', u'ΥΣ', u'ΟΥ', u'ΑΣ', u'ΗΣ', u'ΟΣ', u'ΕΣ', u'ΕΑ', u'ΩΝ', u'ΤΙ', u'ΕΙ',
                  u'ΟΝ', u'ΑΝ', u'ΕΝ', u'ΙΝ', u'ΟΙ', u'Η', u'Α', u'Ο',  u'Ι', u'Υ', u'Ε']

        for ii in range(len(suffix)):
            if ends_with(word, suffix[ii]) and (len(word) - len(suffix[ii])) > 1:
                return word[:len(word) - len(suffix[ii])]

    # rule-set 5 --- Singular Noun
    elif pos in ['NNM', 'NNF', 'NNN', 'NNPM', 'NNPF', 'NNPN']:

        if pos in ['NNF', 'NNPF']:
            if word[-3:] in [u'ΕΑΣ', u'ΙΑΣ'] and len(word[:-2]) > 1:
                return word[:-2]

        suffix = [u'ΟΥΣ', u'ΕΩΣ', u'ΕΟΣ', u'ΟΥΝ', u'ΕΙΣ', u'ΥΣ', u'ΩΣ', u'ΟΥ', u'ΑΣ', u'ΗΣ', u'ΟΣ', u'ΕΣ', u'ΩΝ', u'ΕΙ', u'ΟΝ', u'ΑΝ', u'ΕΝ', u'ΙΝ',
                  u'ΟΙ', u'ΙΣ', u'Η', u'Α', u'Ω', u'Ο', u'Ι', u'Ε']
        for ii in range(len(suffix)):
            if ends_with(word, suffix[ii]) and (len(word) - len(suffix[ii])) > 0:
                return word[:len(word) - len(suffix[ii])]

    # rule-set 6 --- Plural Noun
    elif pos in ['NNSM', 'NNSF', 'NNSN', 'NNPSM', 'NNPSF', 'NNPSN']:
        suffix = [u'ΕΙΣΕΣ', u'ΕΙΣΩΝ', u'ΙΑΔΕΣ', u'ΙΑΔΩΝ', u'ΟΥΔΕΣ', u'ΟΥΔΩΝ', u'ΙΜΑΤΑ', u'ΟΥΣ', u'ΕΙΣ', u'ΕΩΝ', u'ΟΙ', u'ΩΝ', u'ΕΣ', u'ΕΑ', u'Α',
                  u'Η']
        for ii in range(len(suffix)):
            if ends_with(word, suffix[ii]) and (len(word) - len(suffix[ii])) > 0:
                return word[:len(word) - len(suffix[ii])]

    # rule-set 7 --- Adverb
    elif pos == 'RB':
        suffix = [u'ΟΥΣΤΑΤΑ', u'ΑΙΤΕΡΑ', u'ΑΙΤΕΡΩΣ', u'ΟΤΑΤΑ', u'ΕΣΤΑΤΑ', u'ΥΤΑΤΑ', u'ΟΤΕΡΟ', u'ΟΤΕΡΑ', u'ΕΣΤΕΡΑ', u'ΑΙΤΕΡΑ', u'ΥΤΕΡΑ', u'ΑΣΙΑ',
                  u'ΜΕΝΑ', u'ΕΩΣ', u'ΤΑΤΑ', u'ΩΣ', u'ΟΥ', u'Α', u'Υ', u'Ο']
        for ii in range(len(suffix)):
            if ends_with(word, suffix[ii]) and (len(word) - len(suffix[ii])) > 0:
                return word[:len(word) - len(suffix[ii])]

    # rule-set 8 ---> irregular adjectives
    for cur_word in irregular_adjectives:		# for every word in irregular adjective
        suf = len(word)-len(cur_word) 	        # number of additional letters-suffix
        if word[:-suf] == cur_word:
            suffix = [u'ΤΕΡΟΥΣ', u'ΤΕΡΟΣ', u'ΤΕΡΟΝ', u'ΤΕΡΟΥ', u'ΤΕΡΗΣ', u'ΤΕΡΟΙ', u'ΤΕΡΩΝ', u'ΤΕΡΕΣ', u'ΤΑΤΟΣ', u'ΤΑΤΟΥ', u'ΤΑΤΗΣ', u'ΤΑΤΟΙ',
                      u'ΤΑΤΩΝ', u'ΤΑΤΕΣ', u'ΤΕΡΟ', u'ΤΕΡΗ', u'ΤΕΡΑ', u'ΤΑΤΟ', u'ΤΑΤΗ', u'ΤΑΤΑ']
            for ii in range(len(suffix)):
                if ends_with(word, suffix[ii]):
                    return word[:len(word) - len(suffix[ii])]

    return word
