# -*- coding: utf-8 -*-
#   lemmatize_verb.py is free software: you can redistribute it and/or modify
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

__author__ = "Konstantinos Pechlivanis"
__copyright__ = "Copyright 2016, Greek-Stemmer"
__credits__ = ["Konstantinos Pechlivanis", "Eirini Florou"]
__license__ = "GPL"
__version__ = "1.2.1"
__maintainer__ = "Konstantinos Pechlivanis"
__email__ = "kpechlivanis21@gmail.com"
__status__ = "Production"


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
    # rule-set 1 --- Irregular verbs
    if word in [u'ΕΙΜΑΙ', u'ΕΙΣΑΙ', u'ΕΙΝΑΙ', u'ΕΙΜΑΣΤΕ', u'ΕΙΣΤΕ', u'ΕΙΣΑΣΤΕ']:
        return 'ΕΙ'
    
    if word in [u'ΗΜΟΥΝ', u'ΗΣΟΥΝ', u'ΗΤΑΝΕ', u'ΗΜΟΥΝΑ', u'ΗΣΟΥΝΑ', u'ΗΜΑΣΤΕ', u'ΗΣΑΣΤΕ', u'ΗΜΑΣΤΑΝ', u'ΗΣΑΣΤΑΝ', u'ΗΤΑΝ', u'ΔΩ', u'ΔΕΙΣ', u'ΔΕΙ',
                  u'ΔΟΥΜΕ', u'ΔΕΙΤΕ', u'ΔΟΥΝ', u'ΠΩ', u'ΠΕΙΣ', u'ΠΕΙ', u'ΠΟΥΜΕ', u'ΠΕΙΤΕ', u'ΠΟΥΝ', u'ΖΩ', u'ΖΕΙΣ', u'ΖΕΙ', u'ΖΟΥΜΕ', u'ΖΕΙΤΕ',
                  u'ΖΟΥΝ', u'ΖΟΥΝΕ', u'ΖΟΥΣΑ', u'ΖΟΥΣΕΣ', u'ΖΟΥΣΕ', u'ΖΟΥΣΑΜΕ', u'ΖΟΥΣΑΤΕ', u'ΖΟΥΣΑΝΕ', u'ΖΟΥΣΑΝ']:
        return word[0]

    # rule-set 2 --- ACTIVE VOICE, Singular --- PASSIVE VOICE, Singular
    if pos in ['VB', 'VBD', 'VBF', 'MD']:
        suffix = [u'ΙΟΜΟΥΝΑ', u'ΙΟΣΟΥΝΑ', u'ΟΥΜΟΥΝΑ', u'ΟΥΣΟΥΝΑ', u'ΙΟΜΟΥΝ', u'ΙΟΣΟΥΝ', u'ΙΟΤΑΝΕ', u'ΟΥΣΟΥΝ', u'ΟΥΜΟΥΝ', u'ΟΜΟΥΝΑ', u'ΟΣΟΥΝΑ',
                  u'ΑΡΗΣΕΣ', u'ΩΝΤΑΣ', u'ΟΝΤΑΣ', u'ΟΜΟΥΝ', u'ΟΣΟΥΝ', u'ΟΤΑΝΕ', u'ΟΥΣΑΙ', u'ΟΥΤΑΙ', u'ΟΥΣΕΣ', u'ΑΡΕΙΣ', u'ΙΕΜΑΙ', u'ΙΕΣΑΙ', u'ΙΕΤΑΙ',
                  u'ΟΥΜΑΙ', u'ΕΙΣΑΙ', u'ΕΙΤΑΙ', u'ΙΟΤΑΝ', u'ΑΡΗΣΕ', u'ΑΡΗΣΑ', u'ΕΣΑΙ', u'ΕΤΑΙ', u'ΗΚΕΣ', u'ΟΜΑΙ', u'ΟΤΑΝ', u'ΟΥΣΑ', u'ΟΥΣΕ', u'ΑΓΕΣ',
                  u'ΩΜΑΙ', u'ΑΣΑΙ', u'ΑΤΑΙ', u'ΑΡΕΣ', u'ΑΡΕΙ', u'ΜΑΙ', u'ΣΑΙ', u'ΤΑΙ', u'ΜΗΝ', u'ΗΚΑ', u'ΗΚΕ', u'ΕΙΣ', u'ΑΕΙ', u'ΑΓΑ', u'ΑΓΕ', u'ΟΙΣ',
                  u'ΑΡΩ', u'ΑΡΑ', u'ΑΡΕ', u'ΟΥ', u'ΗΝ', u'ΗΣ', u'ΕΙ', u'ΑΩ', u'ΑΣ', u'ΕΣ', u'ΟΙ', u'ΣΟ', u'ΤΟ', u'Ω', u'Α', u'Ε', u'Η']

        for ii in range(len(suffix)):
            if suffix[ii] == u'ΙΟΤΑΝ' and len(word) > 5:
                if word[-6] in vowels:
                    continue
            if ends_with(word, suffix[ii]) and (len(word) - len(suffix[ii])) > 1:
                return word[:len(word) - len(suffix[ii])]

    # rule-set 3 --- ACTIVE VOICE, Plural --- PASSIVE VOICE, Plural
    if pos in ['VBS', 'VBDS', 'VBFS']:
        suffix = [u'ΙΟΝΤΟΥΣΑΝ', u'ΙΟΜΑΣΤΑΝ', u'ΙΟΣΑΣΤΑΝ', u'ΙΟΥΝΤΑΝΕ', u'ΟΥΜΑΣΤΑΝ', u'ΟΥΣΑΣΤΑΝ', u'ΟΝΤΟΥΣΑΝ', u'ΟΜΑΣΤΑΝ', u'ΟΥΝΤΑΝΕ', u'ΟΣΑΣΤΑΝ',
                  u'ΑΡΗΣΑΜΕ', u'ΑΡΗΣΑΤΕ', u'ΙΟΜΑΣΤΕ', u'ΙΟΣΑΣΤΕ', u'ΙΟΥΝΤΑΙ', u'ΟΥΜΑΣΤΕ', u'ΙΟΝΤΑΝΕ', u'ΙΟΥΝΤΑΝ', u'ΑΓΑΜΕ', u'ΑΓΑΤΕ', u'ΟΥΣΘΕ',
                  u'ΩΜΕΘΑ', u'ΑΡΕΤΕ', u'ΑΡΟΥΝ', u'ΩΝΤΑΣ', u'ΩΝΤΑΙ', u'ΑΡΑΜΕ', u'ΑΡΑΤΕ', u'ΑΡΑΝΕ', u'ΟΝΤΑΣ', u'ΗΚΑΜΕ', u'ΕΙΣΤΕ', u'ΟΝΤΑΙ', u'ΗΚΑΤΕ',
                  u'ΗΚΑΝΕ', u'ΑΓΑΝΕ', u'ΟΝΤΑΝ', u'ΙΕΣΤΕ', u'ΟΥΤΑΝ', u'ΟΥΣΙΝ', u'ΟΥΣΑΝ', u'ΟΥΤΕ', u'ΜΕΘΑ', u'ΝΤΑΙ', u'ΗΜΕΝ', u'ΗΣΕΝ', u'ΗΣΑΝ', u'ΗΚΑΝ',
                  u'ΟΥΜΕ', u'ΟΥΝΕ', u'ΕΙΤΕ', u'ΑΣΘΕ', u'ΑΓΑΝ', u'ΕΣΤΕ', u'ΑΡΑΝ', u'ΩΜΕΝ', u'ΟΥΣΙ', u'ΟΜΕ', u'ΕΤΕ', u'ΑΜΕ', u'ΑΤΕ', u'ΑΝΕ', u'ΟΥΝ',
                  u'ΗΤΕ', u'ΣΘΕ', u'ΝΤΟ', u'ΑΝ', u'ΤΕ']

        for ii in range(len(suffix)):
            if suffix[ii] in [u'ΙΟΥΝΤΑΙ', u'ΙΟΥΝΤΑΝ'] and len(word) > 7:
                if word[-8] in vowels:
                    continue
            if ends_with(word, suffix[ii]) and (len(word) - len(suffix[ii])) > 1:
                return word[:len(word) - len(suffix[ii])]

    return word
