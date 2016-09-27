# -*- coding: utf-8 -*-
# !/usr/bin/python
#########################################################################################################################################
#       THESIS	: Corpus Based Methods for Learning Models of Metaphor in Modern Greek	                                                #
#                                                                                                                                       #
#       AUTHOR	: Konstantinos Pechlivanis                                                                                              #
#                                                                                                                                       #
#       SUMMARY: A collection of functions that read csv or json files from disk and return them                                        #
#                                                                                                                                       #
#       USAGE: Just import and use the functions                                                                                        #
#########################################################################################################################################
import json
import os


class LocalData:

    def __init__(self):
        self.get_pos = get_pos()
        self.close_sets = close_sets()
        self.vowels = vowels()


def get_pos():
    try:
        fn = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        with open(fn + "/data/POS.json") as data_file:
            return json.load(data_file)
    except IOError as io:
        print(io.message)


def close_sets():
    try:
        fn = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        with open(fn + "/data/close_sets.json") as data_file:
            close_set_words = json.load(data_file)
            for key in close_set_words:
                close_set_words[key] = [unicode(w) for w in close_set_words[key]]   # unicode instance of words
            return close_set_words
    except IOError as io:
        print(io.message)


def vowels():
    try:
        fn = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        with open(fn + "/data/vowels.json") as data_file:
            return [unicode(v) for v in json.load(data_file)['vowels']]     # unicode instance of vowels
    except IOError as io:
        print(io.message)
