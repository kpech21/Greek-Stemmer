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
    :param word:
    :param suffix:
    :return:
    """
    return word[len(word) - len(suffix):] == suffix


def stem(word, pos, is_unlemmatized_word, has_extra_sigma, irregular_adjectives, has_lemma_endon, has_lemma_plision, has_lemma_protimo, numbers):
    """
    :param word:
    :param pos:
    :param is_unlemmatized_word:
    :param has_extra_sigma:
    :param irregular_adjectives:
    :param has_lemma_endon:
    :param has_lemma_plision:
    :param has_lemma_protimo:
    :param numbers:
    :return:
    """

    # rule-set 1Α ---> non-cases
    if word in is_unlemmatized_word:   # maintain word as initial
        return word

    # rule-set 1Β ---> ΕΝΔΟΝ
    elif word in has_lemma_endon:
        return 'ΕΝΔΟΝ'

    # rule-set 1Γ ---> ΠΛΗΣΙΟΝ
    elif word in has_lemma_plision:
        return 'ΠΛΗΣΙΟΝ'

    # rule-set 1Δ ---> ΠΡΟΤΙΜΩ
    elif word in has_lemma_protimo:
        return 'ΠΡΟΤΙΜΩ'

    # rule-set 1Δ ---> Numbers
    elif word in numbers:
        return word

    # rule-set 2 ---> noun with extra sigma
    if word in has_extra_sigma:
        return word.decode('utf-8')[:-1]

    # rule-set 3 ---> neuter noun with suffix ΜΑΤΟΣ, ΜΑΤΑ, ΜΑΤΩΝ, ΜΑ
    if pos in ['NNN', 'NNSN', 'NNPN', 'NNPSN']:
        for suffix in ['ΜΑΤΟΣ', 'ΜΑΤΩΝ', 'ΜΑΤΑ', 'ΜΑ']:
            if ends_with(word, suffix):
                return word[:len(word) - len(suffix)] + 'Μ'

    # rule-set 4 ---> suffix for proper names
    if pos in ['NNPM', 'NNPF', 'NNPN', 'NNPSM', 'NNPSF', 'NNPSN']:
        for suffix in ['ΟΝΟΣ', 'ΩΝΟΣ', 'ΟΡΟΣ', 'ΕΥΣ', 'ΕΩΣ', 'ΟΝΤΟΣ', 'ΚΤΟΣ', 'ΟΥΣ']:
            if ends_with(word, suffix):
                return word[:len(word) - len(suffix)]
        for suffix in ['ΩΝ', 'ΩΡ', 'ΙΣ', 'Ξ', 'Ω', 'ΩΣ']:
            if ends_with(word, suffix):
                return word[:len(word) - len(suffix)]

    # rule-set 5 ---> irregular adjective
    for cur_word in irregular_adjectives:		# for every word in irregular adjective
        suf = len(word)-len(cur_word) 	# number of additional letters-suffix
        if word[:-suf] == cur_word:
            for suffix in ['ΤΕΡΟΥΣ', 'ΤΕΡΟΣ', 'ΤΕΡΟΝ', 'ΤΕΡΟΥ', 'ΤΕΡΗΣ', 'ΤΕΡΟΙ', 'ΤΕΡΩΝ', 'ΤΕΡΕΣ', 'ΤΑΤΟΣ', 'ΤΑΤΟΥ', 'ΤΑΤΗΣ', 'ΤΑΤΟΙ',
                           'ΤΑΤΩΝ', 'ΤΑΤΕΣ']:
                if ends_with(word, suffix):
                    return word[:len(word) - len(suffix)]
            for suffix in ['ΤΕΡΟ', 'ΤΕΡΗ', 'ΤΕΡΑ', 'ΤΑΤΟ', 'ΤΑΤΗ', 'ΤΑΤΑ']:
                if ends_with(word, suffix):
                    return word[:len(word) - len(suffix)]

    # rule-set 6 ---> Adjectives AND Participles
    if ('JJ' in pos) or (pos == 'CD') or (pos in ['VBG', 'VBP', 'VBPD', 'PRP', 'PP', 'REP', 'DP', 'IP', 'WP', 'QP', 'INP']):
        med_suffix = ['ΜΕΝΟΣ', 'ΜΕΝΟΥ', 'ΜΕΝΗΣ', 'ΜΕΝΟΙ', 'ΜΕΝΩΝ', 'ΩΜΕΝΟ', 'ΩΜΕΝΗ', 'ΩΜΕΝΑ', 'ΥΤΕΡΑ', 'ΥΤΑΤΑ', 'ΥΤΕΡΟ', 'ΟΤΑΤΗ', 'ΜΕΝΕΣ',
                      'ΟΜΕΝΑ', 'ΩΜΕΝΟ', 'ΩΜΕΝΗ', 'ΟΤΕΡΟ', 'ΟΤΕΡΗ', 'ΕΙΣΕΣ', 'ΟΜΕΝΟ', 'ΟΜΕΝΗ', 'ΥΤΕΡΗ', 'ΟΤΕΡΑ', 'ΜΕΝΟΙ', 'ΥΤΑΤΗ', 'ΟΤΑΤΟ',
                      'ΟΤΑΤΑ', 'ΜΕΝΟΥ', 'ΜΕΝΟΣ', 'ΗΜΕΝΗ', 'ΜΕΝΩΝ', 'ΜΕΝΗΣ', 'ΗΜΕΝΟ', 'ΗΜΕΝΑ', 'ΟΝΤΑΣ', 'ΩΝΤΑΣ', 'ΩΤΕΡΟ', 'ΩΤΕΡΕ', 'ΩΤΕΡΗ',
                      'ΩΤΕΡΑ', 'ΩΤΑΤΟ', 'ΩΤΑΤΕ', 'ΩΤΑΤΗ', 'ΩΤΑΤΑ']
        mdbig_suffix = ['ΥΤΕΡΕΣ', 'ΩΜΕΝΟΥ', 'ΟΤΑΤΩΝ', 'ΕΣΤΑΤΟ', 'ΕΣΤΑΤΗ', 'ΥΤΑΤΩΝ', 'ΥΤΕΡΗΣ', 'ΟΜΕΝΟΣ', 'ΟΤΕΡΟΙ', 'ΟΤΕΡΩΝ', 'ΥΤΑΤΟΣ', 'ΥΤΑΤΟΥ',
                        'ΕΣΤΑΤΑ', 'ΥΤΑΤΗΣ', 'ΟΤΕΡΟΣ', 'ΟΤΕΡΟΥ', 'ΥΤΑΤΕΣ', 'ΟΤΕΡΕΣ', 'ΥΤΕΡΟΙ', 'ΥΤΕΡΩΝ', 'ΑΙΤΕΡΟ', 'ΟΤΕΡΗΣ', 'ΥΤΕΡΟΣ', 'ΑΙΤΕΡΗ',
                        'ΑΙΤΕΡΑ', 'ΜΕΝΟΥΣ', 'ΥΤΕΡΟΥ', 'ΩΜΕΝΗΣ', 'ΩΜΕΝΩΝ', 'ΩΜΕΝΕΣ', 'ΟΥΜΕΝΟ', 'ΟΥΜΕΝΗ', 'ΟΥΜΕΝΑ', 'ΟΜΕΝΕΣ', 'ΩΜΕΝΟΣ', 'ΟΜΕΝΗΣ',
                        'ΟΜΕΝΩΝ', 'ΕΣΤΕΡΟ', 'ΕΣΤΕΡΗ', 'ΕΣΤΕΡΑ', 'ΟΤΑΤΟΣ', 'ΟΤΑΤΗΣ', 'ΟΜΕΝΟΥ', 'ΟΤΑΤΟΙ', 'ΥΤΑΤΟΙ', 'ΟΤΑΤΟΥ', 'ΗΜΕΝΗΣ', 'ΟΜΕΝΟΙ',
                        'ΗΜΕΝΟΥ', 'ΗΜΕΝΟΙ', 'ΗΜΕΝΩΝ', 'ΜΕΝΟΥΣ', 'ΗΜΕΝΟΣ', 'ΩΜΕΝΟΙ', 'ΟΤΑΤΕΣ', 'ΩΤΕΡΟΣ', 'ΩΤΕΡΟΥ', 'ΩΤΕΡΟΝ', 'ΩΤΕΡΟΙ', 'ΩΤΕΡΩΝ',
                        'ΩΤΕΡΗΣ', 'ΩΤΕΡΕΣ', 'ΩΤΕΡΑΣ', 'ΩΤΑΤΟΣ', 'ΩΤΑΤΟΥ', 'ΩΤΑΤΟΙ', 'ΩΤΑΤΩΝ', 'ΩΤΑΤΗΣ', 'ΩΤΑΤΕΣ']
        big_suffix = ['ΥΤΕΡΟΥΣ', 'ΕΣΤΕΡΟΙ', 'ΕΣΤΕΡΩΝ', 'ΕΣΤΕΡΕΣ', 'ΟΥΣΤΕΡΗ', 'ΩΜΕΝΟΥΣ', 'ΕΣΤΑΤΗΣ', 'ΕΣΤΕΡΑΣ', 'ΕΣΤΕΡΗΣ', 'ΟΥΣΤΕΡΟ', 'ΑΣΜΕΝΟΙ',
                      'ΟΤΕΡΟΥΣ', 'ΕΣΤΑΤΟΥ', 'ΕΣΤΑΤΟΣ', 'ΟΥΣΤΕΡΑ', 'ΕΣΤΑΤΕΣ', 'ΥΤΑΤΟΥΣ', 'ΕΣΤΕΡΟΥ', 'ΕΣΤΕΡΟΣ', 'ΑΙΤΕΡΟΣ', 'ΑΙΤΕΡΟΥ', 'ΕΣΤΑΤΟΙ',
                      'ΑΙΤΕΡΟΙ', 'ΑΙΤΕΡΩΝ', 'ΑΙΤΕΡΗΣ', 'ΑΙΤΕΡΑΣ', 'ΟΥΜΕΝΟΥ', 'ΟΥΜΕΝΟΣ', 'ΟΥΜΕΝΗΣ', 'ΟΥΜΕΝΩΝ', 'ΟΥΜΕΝΕΣ', 'ΟΜΕΝΟΥΣ', 'ΕΣΤΑΤΩΝ',
                      'ΕΣΤΕΡΟΝ', 'ΗΜΕΝΟΥΣ', 'ΟΥΣΤΑΤΗ', 'ΟΥΣΤΑΤΑ', 'ΕΣΤΕΡΟΝ', 'ΟΥΣΤΑΤΟ', 'ΩΤΕΡΟΥΣ', 'ΩΤΑΤΟΥΣ']
        exbig_suffix = ['ΟΥΣΤΕΡΟΥ', 'ΟΥΣΤΕΡΟΣ', 'ΕΣΤΕΡΟΥΣ', 'ΟΥΣΤΕΡΗΣ', 'ΕΣΤΑΤΟΥΣ', 'ΟΥΣΤΕΡΩΝ', 'ΟΥΣΤΑΤΕΣ', 'ΟΥΣΤΕΡΕΣ', 'ΟΥΣΤΕΡΟΙ', 'ΑΙΤΕΡΟΥΣ',
                        'ΟΥΣΤΑΤΟΣ', 'ΟΥΣΤΑΤΟΥ', 'ΟΥΣΤΑΤΗΣ', 'ΟΥΣΤΑΤΩΝ']

        for suffix in ['ΟΥΣΤΕΡΟΥΣ', 'ΟΥΣΤΑΤΟΥΣ']:
            if ends_with(word, suffix):
                if (len(word.decode('utf-8')) - len(suffix.decode('utf-8'))) > 1:
                    return word[:len(word) - len(suffix)]
        for suffix in exbig_suffix:
            if ends_with(word, suffix):
                if (len(word.decode('utf-8')) - len(suffix.decode('utf-8'))) > 1:
                    return word[:len(word) - len(suffix)]
        for suffix in big_suffix:
            if ends_with(word, suffix):
                if (len(word.decode('utf-8')) - len(suffix.decode('utf-8'))) > 1:
                    return word[:len(word) - len(suffix)]
        for suffix in mdbig_suffix:
            if ends_with(word, suffix):
                if (len(word.decode('utf-8')) - len(suffix.decode('utf-8'))) > 1:
                    return word[:len(word) - len(suffix)]
        for suffix in med_suffix:
            if ends_with(word, suffix):
                if (len(word.decode('utf-8')) - len(suffix.decode('utf-8'))) > 1:
                    return word[:len(word) - len(suffix)]
        for suffix in ['ΜΕΝΟ', 'ΜΕΝΗ', 'ΜΕΝΑ', 'ΕΙΕΣ', 'ΕΙΩΝ']:
            if ends_with(word, suffix):
                if (len(word.decode('utf-8')) - len(suffix.decode('utf-8'))) > 1:
                    return word[:len(word) - len(suffix)]
        for suffix in ['ΟΥΣ', 'ΕΩΣ', 'ΕΟΣ', 'ΩΣΑ', 'ΟΥΝ', 'ΕΙΣ', 'ΟΥΣ', 'ΕΩΝ']:
            if ends_with(word, suffix):
                if (len(word.decode('utf-8')) - len(suffix.decode('utf-8'))) > 1:
                    return word[:len(word) - len(suffix)]
        for suffix in ['ΙΣ', 'ΟΣ', 'ΥΣ', 'ΟΥ', 'ΑΣ', 'ΗΣ', 'ΟΣ', 'ΕΣ', 'ΕΑ', 'ΩΝ', 'ΤΙ', 'ΕΙ', 'ΟΝ', 'ΑΝ', 'ΕΝ', 'ΙΝ', 'ΟΙ']:
            if ends_with(word, suffix):
                if (len(word.decode('utf-8')) - len(suffix.decode('utf-8'))) > 1:
                    return word[:len(word) - len(suffix)]
        for suffix in ['Η', 'Α', 'Ο',  'Ι', 'Υ', 'Ε'] :
            if ends_with(word, suffix):
                if (len(word.decode('utf-8')) - len(suffix.decode('utf-8'))) > 0:
                    return word[:len(word) - len(suffix)]

    # rule-set 7 --- Singular Noun
    elif pos in ['NNM', 'NNF', 'NNN', 'NNPM', 'NNPF', 'NNPN']:

        if pos in ['NNF', 'NNPF']:
            if word.decode('utf-8')[-3:] in ['ΕΑΣ', 'ΙΑΣ'] :
                if len(word.decode('utf-8')[:-2]) > 1:
                    return word.decode('utf-8')[:-2].encode('utf-8')
        for suffix in ['ΟΥΣ', 'ΕΩΣ', 'ΕΟΣ', 'ΟΥΝ', 'ΕΙΣ']:
            if (pos in ['NNF', 'NNPF']) and (suffix == 'ΤΗΣ'):  # if word is female and suffix is -ΤΗΣ
                continue
            if ends_with(word, suffix):
                if (len(word.decode('utf-8')) - len(suffix.decode('utf-8'))) > 0:
                    return word[:len(word) - len(suffix)]
        for suffix in ['ΥΣ', 'ΩΣ', 'ΟΥ', 'ΑΣ', 'ΗΣ', 'ΟΣ', 'ΕΣ', 'ΩΝ', 'ΕΙ', 'ΟΝ', 'ΑΝ', 'ΕΝ', 'ΙΝ', 'ΟΙ', 'ΙΣ']:
            if ends_with(word, suffix):
                if (len(word.decode('utf-8')) - len(suffix.decode('utf-8'))) > 0:
                    return word[:len(word) - len(suffix)]
        for suffix in ['Η', 'Α', 'Ω', 'Ο',  'Ι', 'Ε'] :
            if ends_with(word, suffix):
                if (len(word.decode('utf-8')) - len(suffix.decode('utf-8'))) > 0:
                    return word[:len(word) - len(suffix)]

    # rule-set 8 --- Plural Noun
    elif pos in ['NNSM', 'NNSF', 'NNSN', 'NNPSM', 'NNPSF', 'NNPSN']:
        for suffix in ['ΕΙΣΕΣ', 'ΕΙΣΩΝ', 'ΙΑΔΕΣ', 'ΙΑΔΩΝ', 'ΟΥΔΕΣ', 'ΟΥΔΩΝ', 'ΙΜΑΤΑ']:
            if ends_with(word, suffix):
                if (len(word.decode('utf-8')) - len(suffix.decode('utf-8'))) > 0:
                    return word[:len(word) - len(suffix)]
        for suffix in ['ΟΥΣ', 'ΕΙΣ', 'ΕΩΝ']:
            if ends_with(word, suffix):
                if (len(word.decode('utf-8')) - len(suffix.decode('utf-8'))) > 0:
                    return word[:len(word) - len(suffix)]
        for suffix in ['ΟΙ', 'ΩΝ', 'ΕΣ', 'ΕΑ']:
            if ends_with(word, suffix):
                if (len(word.decode('utf-8')) - len(suffix.decode('utf-8'))) > 0:
                    return word[:len(word) - len(suffix)]
        for suffix in ['Α', 'Η']:
            if ends_with(word, suffix):
                if (len(word.decode('utf-8')) - len(suffix.decode('utf-8'))) > 0:
                    return word[:len(word) - len(suffix)]

    # rule-set 9 --- Adverb
    elif pos == 'RB':
        for suffix in ['ΟΥΣΤΑΤΑ', 'ΑΙΤΕΡΑ', 'ΑΙΤΕΡΩΣ', 'ΟΤΑΤΑ', 'ΕΣΤΑΤΑ', 'ΥΤΑΤΑ']:
            if ends_with(word, suffix):
                if (len(word.decode('utf-8')) - len(suffix.decode('utf-8'))) > 0:
                    return word[:len(word) - len(suffix)]
        for suffix in ['ΟΤΕΡΟ', 'ΟΤΕΡΑ', 'ΕΣΤΕΡΑ', 'ΑΙΤΕΡΑ', 'ΥΤΕΡΑ', 'ΑΣΙΑ', 'ΜΕΝΑ', 'ΕΩΣ', 'ΤΑΤΑ']:
            if ends_with(word, suffix):
                if (len(word.decode('utf-8')) - len(suffix.decode('utf-8'))) > 0:
                    return word[:len(word) - len(suffix)]      
        for suffix in ['ΩΣ', 'ΟΥ'] :
            if ends_with(word, suffix):
                if (len(word.decode('utf-8')) - len(suffix.decode('utf-8'))) > 0:
                    return word[:len(word) - len(suffix)]
        for suffix in ['Α', 'Υ', 'Ο'] :
            if ends_with(word, suffix):
                if (len(word.decode('utf-8')) - len(suffix.decode('utf-8'))) > 0:
                    return word[:len(word) - len(suffix)]

    return word
