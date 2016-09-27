# -*- coding: utf-8 -*-
# !/usr/bin/python

import unicodedata

from src import lemmatize_non_verb, lemmatize_verb
from src.load_json_data import LocalData


def run():

    load_data = LocalData()
    total_pos = [item for pos in load_data.get_pos.values() for item in pos]  # load the total number of POS in a list

    while True:

        word = unicode(raw_input('Please give a word: ').strip(), 'utf-8')

        pos = raw_input('Please give the Part-of-Speech of word: ').strip()
        while pos not in total_pos:
            print 'Wrong Part-of-Speech Tag! The available POS are:\n\n   ' + ', '.join(total_pos) + '\n'
            pos = raw_input('Please give the Part-of-Speech of word correctly: ').strip()

        # Remove accents - Upper case
        word = word.upper()
        nkfd_form = unicodedata.normalize('NFKD', word)
        word = "".join([c for c in nkfd_form if not unicodedata.combining(c)])

        if pos == 'FW':  # case of non-Greek word
            print 'Non-Greek word'

        elif pos in load_data.get_pos['Verb']:  # if given word is verb or modal verb
            word = lemmatize_verb.stem(word, pos, load_data.vowels)

        else:  # rest of cases
            word = lemmatize_non_verb.stem(word, pos, load_data.close_sets['is_unlemmatized_word'], load_data.close_sets['has_extra_sigma'],
                                           load_data.close_sets['irregular_adjectives'], load_data.close_sets['has_lemma_endon'],
                                           load_data.close_sets['has_lemma_plision'], load_data.close_sets['has_lemma_protimo'],
                                           load_data.close_sets['numbers'])
        print word


if __name__ == "__main__":
    run()
