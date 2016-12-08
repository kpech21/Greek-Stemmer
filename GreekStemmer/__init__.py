# -*- coding: utf-8 -*-
# !/usr/bin/python
#   __init__.py is free software: you can redistribute it and/or modify
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


from __future__ import print_function
from .suffixes import lemmatize_verb, lemmatize_non_verb
from io import open

import sys
import os
import unicodedata
import json

__author__ = 'Konstantinos Pechlivanis'
__copyright__ = 'Copyright 2016, Greek-Stemmer'
__credits__ = ['Konstantinos Pechlivanis', 'Eirini Florou']
__license__ = 'GPL'
__version__ = '1.2.10'
__maintainer__ = 'Konstantinos Pechlivanis'
__email__ = 'kpechlivanis21@gmail.com'
__status__ = 'Production'

__all__ = ['GreekStemmer']

# the greek alphabet
ALPHABET = frozenset(u'ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ')

# the greek vowels
VOWELS = frozenset(u'ΑΕΗΙΟΥΩ')

# the file that contains the set of part of speech.
DEFAULT_POS_OF_WORDS_FILE = 'POS.json'

# the file that contains the set of word sets.
DEFAULT_WORD_SETS_FILE = 'word_sets.json'


class Stemmer:
    """
    Stemmer for greek words
        :var:
        pos_words (set): set of POS words. (default: DEFAULT_POS_OF_WORDS_FILE)
        word_sets (set): set of word sets. (default: DEFAULT_WORD_SETS_FILE)
    """

    def __init__(self, **kwargs):
        self.pos_words = kwargs.get('pos_words', DefaultSetHolder.DEFAULT_POS_OF_WORDS_FILE)
        self.total_pos = [item for pos in self.pos_words.values() for item in pos]
        self.word_sets = kwargs.get('word_sets', DefaultSetHolder.DEFAULT_WORD_SETS_FILE)

    def stem_word(self, word, pos):
        """
        Finds the stem of a given word.
        :param: word (str): the word to stem
        :returns: str: the stemmed word
        """

        word = word_paring(word)
        pos = pos_parsing(pos)

        if not self.proceed_to_stem(word, pos):
            return word

        if pos in self.pos_words['Verb']:  # if given word is verb or modal verb
            word = lemmatize_verb.stem(word, pos, VOWELS)

        else:  # rest of cases
            word = lemmatize_non_verb.stem(word, pos, self.word_sets['unlemmatized'], self.word_sets['extra_sigma'],
                                           self.word_sets['irregular_adjectives'], self.word_sets['lemma_endon'],
                                           self.word_sets['lemma_plision'], self.word_sets['lemma_protimo'],
                                           self.word_sets['numbers'])
        return word

    def proceed_to_stem(self, word, pos):
        """
        Checks whether a stem process should proceed or not.
        :param: word (str): the word to check for stem
        :returns: bool: whether to proceed or not
        """
        if not word:
            raise ValueError('There is no given word')

        if pos not in self.total_pos:
            raise ValueError('[There is no valid Part-of-Speech')

        if not is_greek(word):
            raise ValueError('There is no greek word')

        if len(word) < 2:
            raise ValueError('There is no valid word')

        return True


def word_paring(word):
    """
    Parses a word.
    :param: word (str): the word to parse
    :returns: str: the parsed word
    """
    # convert the given word to unicode and uppercase
    word = unicode(word.strip(), 'utf-8').upper()
    # remove accents
    nkfd_form = unicodedata.normalize('NFKD', word)
    word = ''.join([c for c in nkfd_form if not unicodedata.combining(c)])
    return word


def pos_parsing(pos):
    """
    Parses of POS
    :param: POS (str): part of speech
    :return: str: the parsed pos
    """
    return pos.strip().upper()


def is_greek(word):
    """
    Checks whether a word is written in greek language or not.
    :param: word (str): the word to check its letters
    :returns: bool: whether contains only greek letters or not.
    """
    return all(n in ALPHABET for n in word)


def load_word_set(name_file):
    """
    Creates a set from a json file
    :param: name_file (str): relative path to file
    :returns: set: the set of words
    """
    try:
        path_to_file = os.path.join(os.path.dirname(__file__), 'resources', name_file)
        with open(path_to_file, encoding='utf-8') as fout:
            results = json.load(fout)
            for json_set in results:
                results[json_set] = frozenset(unicode(x) for x in results[json_set])  # unicode instance of words
            return results
    except IOError:
        print('Unable to load {}', name_file, file=sys.stderr)


class DefaultSetHolder:
    def __init__(self):
        pass

    DEFAULT_POS_OF_WORDS_FILE = load_word_set(DEFAULT_POS_OF_WORDS_FILE)
    DEFAULT_WORD_SETS_FILE = load_word_set(DEFAULT_WORD_SETS_FILE)
