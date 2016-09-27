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
#       SUMMARY : this function finds the lemma of words (verbs), function "stem" estimates the lemma and function "ends_with"          #
#                 estimates the suffix                                                                                                  #
#                                                                                                                                       #
#       USAGE	: python metaphor_detection_term.py	sys.argv[1] sys.argv[2]	sys.argv[3] sys.argv[4] sys.argv[5] sys.argv[6]	sys.argv[7] #
#                                                                                                                                       #
#       OUTPUTS	: return the lemma of word                                                                                              #
#########################################################################################################################################


def ends_with(word, suffix):
    """
    :param word: string, required
    :param suffix: string, required
    :return: bool
        -Return True if the word has a specific suffix, othrewise return False
    """
    return word[len(word) - len(suffix):] == suffix


def stem(word, pos, vowels):
    """
    :param word: string, required
    :param pos: string, required
    :param vowels: list, required
        -A list with the total number of greek vowels
    :return: string
        -Return the lemmatized word
    """
    # rule-set 1 --- Specific verbs
    if word in [u'ΕΙΜΑΙ', u'ΕΙΣΑΙ', u'ΕΙΝΑΙ', u'ΕΙΜΑΣΤΕ', u'ΕΙΣΤΕ', u'ΕΙΣΑΣΤΕ']:
        return 'ΕΙ'
    elif word in [u'ΗΜΟΥΝ', u'ΗΣΟΥΝ', u'ΗΤΑΝΕ', u'ΗΜΟΥΝΑ', u'ΗΣΟΥΝΑ', u'ΗΜΑΣΤΕ', u'ΗΣΑΣΤΕ', u'ΗΜΑΣΤΑΝ', u'ΗΣΑΣΤΑΝ', u'ΗΤΑΝ']:
        return 'Η'
    elif word in [u'ΔΩ', u'ΔΕΙΣ', u'ΔΕΙ', u'ΔΟΥΜΕ', u'ΔΕΙΤΕ', u'ΔΟΥΝ', u'ΠΩ', u'ΠΕΙΣ', u'ΠΕΙ', u'ΠΟΥΜΕ', u'ΠΕΙΤΕ', u'ΠΟΥΝ', u'ΖΩ', u'ΖΕΙΣ', u'ΖΕΙ',
                  u'ΖΟΥΜΕ', u'ΖΕΙΤΕ', u'ΖΟΥΝ', u'ΖΟΥΝΕ', u'ΖΟΥΣΑ', u'ΖΟΥΣΕΣ', u'ΖΟΥΣΕ', u'ΖΟΥΣΑΜΕ', u'ΖΟΥΣΑΤΕ', u'ΖΟΥΣΑΝΕ', u'ΖΟΥΣΑΝ']:
        return word[0]

    # rule-set 2 --- ACTIVE VOICE, Singular --- PASSIVE VOICE, Singular
    if pos in ['VB', 'VBD', 'VBF', 'MD']:
        for suffix in [u'ΙΟΜΟΥΝΑ', u'ΙΟΣΟΥΝΑ', u'ΟΥΜΟΥΝΑ', u'ΟΥΣΟΥΝΑ']:
            if ends_with(word, suffix) and (len(word) - len(suffix)) > 1:
                return word[:len(word) - len(suffix)]
        for suffix in [u'ΙΟΜΟΥΝ', u'ΙΟΣΟΥΝ', u'ΙΟΤΑΝΕ', u'ΟΥΣΟΥΝ', u'ΟΥΜΟΥΝ', u'ΟΜΟΥΝΑ', u'ΟΣΟΥΝΑ', u'ΑΡΗΣΕΣ']:
            if ends_with(word, suffix) and (len(word) - len(suffix)) > 1:
                return word[:len(word) - len(suffix)]
        for suffix in [u'ΩΝΤΑΣ', u'ΟΝΤΑΣ', u'ΟΜΟΥΝ', u'ΟΣΟΥΝ', u'ΟΤΑΝΕ', u'ΟΥΣΑΙ', u'ΟΥΤΑΙ', u'ΟΥΣΕΣ', u'ΑΡΕΙΣ', u'ΙΕΜΑΙ', u'ΙΕΣΑΙ', u'ΙΕΤΑΙ',
                       u'ΟΥΜΑΙ', u'ΕΙΣΑΙ', u'ΕΙΤΑΙ', u'ΙΟΤΑΝ', u'ΑΡΗΣΕ', u'ΑΡΗΣΑ']:
            if suffix == u'ΙΟΤΑΝ' and (len(word.decode('utf-8')) > 5):
                if word.decode('utf-8')[-6] in vowels:
                    continue
            if ends_with(word, suffix) and (len(word) - len(suffix)) > 1:
                return word[:len(word) - len(suffix)]
        for suffix in [u'ΕΣΑΙ', u'ΕΤΑΙ', u'ΗΚΕΣ', u'ΟΜΑΙ', u'ΟΤΑΝ', u'ΟΥΣΑ', u'ΟΥΣΕ', u'ΑΓΕΣ', u'ΩΜΑΙ', u'ΑΣΑΙ', u'ΑΤΑΙ', u'ΑΡΕΣ', u'ΑΡΕΙ']:
            if ends_with(word, suffix) and (len(word) - len(suffix)) > 1:
                return word[:len(word) - len(suffix)]
        for suffix in [u'ΜΑΙ', u'ΣΑΙ', u'ΤΑΙ', u'ΜΗΝ', u'ΗΚΑ', u'ΗΚΕ', u'ΕΙΣ', u'ΑΕΙ', u'ΑΓΑ', u'ΑΓΕ', u'ΟΙΣ', u'ΑΡΩ', u'ΑΡΑ', u'ΑΡΕ']:
            if ends_with(word, suffix) and (len(word) - len(suffix)) > 1:
                return word[:len(word) - len(suffix)]
        for suffix in [u'ΟΥ', u'ΗΝ', u'ΗΣ', u'ΕΙ', u'ΑΩ', u'ΑΣ', u'ΕΣ', u'ΟΙ', u'ΣΟ', u'ΤΟ']:
            if ends_with(word, suffix) and (len(word) - len(suffix)) > 1:
                return word[:len(word) - len(suffix)]
        for suffix in [u'Ω', u'Α', u'Ε', u'Η']:
            if ends_with(word, suffix) and (len(word) - len(suffix)) > 1:
                return word[:len(word) - len(suffix)]

    # rule-set 3 --- ACTIVE VOICE, Plural --- PASSIVE VOICE, Plural
    elif pos in ['VBS', 'VBDS', 'VBFS']:
        for suffix in [u'ΙΟΝΤΟΥΣΑΝ', u'ΙΟΜΑΣΤΑΝ', u'ΙΟΣΑΣΤΑΝ', u'ΙΟΥΝΤΑΝΕ', u'ΟΥΜΑΣΤΑΝ', u'ΟΥΣΑΣΤΑΝ']:
            if ends_with(word, suffix) and (len(word) - len(suffix)) > 1:
                return word[:len(word) - len(suffix)]
        for suffix in [u'ΟΝΤΟΥΣΑΝ', u'ΟΜΑΣΤΑΝ', u'ΟΥΝΤΑΝΕ', u'ΟΣΑΣΤΑΝ', u'ΑΡΗΣΑΜΕ', u'ΑΡΗΣΑΤΕ', u'ΙΟΜΑΣΤΕ', u'ΙΟΣΑΣΤΕ', u'ΙΟΥΝΤΑΙ', u'ΟΥΜΑΣΤΕ',
                       u'ΙΟΝΤΑΝΕ', u'ΙΟΥΝΤΑΝ']:
            if suffix in [u'ΙΟΥΝΤΑΙ', u'ΙΟΥΝΤΑΝ'] and len(word.decode('utf-8')) > 7:
                if word.decode('utf-8')[-8] in vowels:
                    continue
            if ends_with(word, suffix) and (len(word) - len(suffix)) > 1:
                return word[:len(word) - len(suffix)]
        for suffix in [u'ΟΥΝΤΑΝ', u'ΙΟΝΤΑΝ', u'ΟΝΤΑΝΕ', u'ΟΥΝΤΑΙ', u'ΟΣΑΣΤΕ', u'ΟΜΑΣΤΕ', u'ΟΥΣΑΜΕ', u'ΟΥΣΑΤΕ', u'ΟΥΣΑΝΕ', u'ΟΥΜΕΘΑ', u'ΑΡΟΥΜΕ',
                       u'ΙΟΝΤΑΙ', u'ΑΡΗΣΑΝ', u'ΟΣΑΣΤΕ']:
            if ends_with(word, suffix) and (len(word) - len(suffix)) > 1:
                return word[:len(word) - len(suffix)]
        for suffix in [u'ΑΓΑΜΕ', u'ΑΓΑΤΕ', u'ΟΥΣΘΕ', u'ΩΜΕΘΑ', u'ΑΡΕΤΕ', u'ΑΡΟΥΝ', u'ΩΝΤΑΣ', u'ΩΝΤΑΙ', u'ΑΡΑΜΕ', u'ΑΡΑΤΕ', u'ΑΡΑΝΕ', u'ΟΝΤΑΣ',
                       u'ΗΚΑΜΕ', u'ΕΙΣΤΕ', u'ΟΝΤΑΙ', u'ΗΚΑΤΕ', u'ΗΚΑΝΕ', u'ΑΓΑΝΕ', u'ΟΝΤΑΝ', u'ΙΕΣΤΕ', u'ΟΥΤΑΝ', u'ΟΥΣΙΝ']:
            if ends_with(word, suffix) and (len(word) - len(suffix)) > 1:
                return word[:len(word) - len(suffix)]
        for suffix in [u'ΟΥΣΑΝ', u'ΟΥΤΕ', u'ΜΕΘΑ', u'ΝΤΑΙ', u'ΗΜΕΝ', u'ΗΣΕΝ', u'ΗΣΑΝ', u'ΗΚΑΝ', u'ΟΥΜΕ', u'ΟΥΝΕ', u'ΕΙΤΕ', u'ΑΣΘΕ', u'ΑΓΑΝ', u'ΕΣΤΕ',
                       u'ΑΡΑΝ', u'ΩΜΕΝ', u'ΟΥΣΙ']:
            if ends_with(word, suffix) and (len(word) - len(suffix)) > 1:
                return word[:len(word) - len(suffix)]
        for suffix in [u'ΟΜΕ', u'ΕΤΕ', u'ΑΜΕ', u'ΑΤΕ', u'ΑΝΕ', u'ΟΥΝ', u'ΗΤΕ', u'ΣΘΕ', u'ΝΤΟ']:
            if ends_with(word, suffix) and (len(word) - len(suffix)) > 1:
                return word[:len(word) - len(suffix)]
        for suffix in [u'ΑΝ', u'ΤΕ']:
            if ends_with(word, suffix) and (len(word) - len(suffix)) > 1:
                return word[:len(word) - len(suffix)]

    return word
