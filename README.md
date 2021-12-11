# Greek Stemmer

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/greek-stemmer-pos?logo=python&logoColor=white)](https://www.python.org/)
[![PyPI](https://img.shields.io/pypi/v/greek-stemmer-pos?color=blue&label=PyPI&logo=PyPI&logoColor=white)](https://pypi.org/project/greek-stemmer-pos/)

![Coverage](https://img.shields.io/badge/Coverage-100%25-orange)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/greek-stemmer-pos?color=orange)](https://www.python.org/dev/peps/pep-0427/)

Python stemming library that given a word and the Part Of Speech tagging (POS) of the word removes its inflectional suffix according to a set of rules based algorithm. The algorithm is developed according to the grammatical rules of the Modern Greek language [1]. An extended documentation of the removal process, as well as a short evaluation of the system is showing the algorithm accuracy that works with better performance than other past stemming algorithms for the Greek language giving 99.4 percent correct results in a dataset of 5000 of words.

[1] David Holton, Peter Mackridge, Ειρήνη Φιλιππάκη-Warburton (2002), "Γραμματική της Ελληνικής Γλώσσας".

POS: The system uses the POS tagger of [Ellogon](https://www.ellogon.org/) with the following [categories](https://www.ellogon.org/index.php/download/all-categories/category/7-ellogon-documentation-manuals#) for the rules:

* Verbs: VB, VBD, VBF, MD, VBS, VBDS, VBFS

* Definite Article : DDT

* Indefinite Article: IDT

* Nouns: NNM, NNF, NNN, NNSM, NNSF, NNSN, NNPM, NNPF, NNPN, NNPSM, NNPSF, NNPSN

* Adjectives: JJM, JJF, JJN, CD, JJSM, JJSF, JJSN

* Pronouns: PRP, PP, REP, DP, IP, WP, QP, INP

* Participles: VBG, VBP, VBPD

* Adverb: RB

* Preposition: INP

Although there is a variety of stemmers, the unique morphological system of each language doesn't allow the creation of
a global rule-based algorithm which would be able to find out the stem of each word. Especially, in some languages with a rich morphological system, like greek, is even more difficult to find the word stem by reducing the suffix from inflected or derived words. At this point, it would be useful to be mentioned that the greek morphological system may appear a wide variety of suffixes, some of them may appear in different parts of speech. For this reason it is necessary to point out the part of speech of the certain word before trying to find out the root of the concrete word. Let's exam some typical examples. For instance, the word "εργαζόμενος" is the participle of the verb "εργάζομαι". Although, the typical suffix of the present participle is "-όμενος", it may be confused with the basic suffix of adjectives  "-ος". As a result can be erroneously be identified as the root of the word "εργαζόμενος", the stem "εργαζόμεν", while in fact its stem is "εργαζ". Moreover, there are numerals or adverbs which may appear typical verbal suffixes. So, the number "οκτώ" or the adverb "παραπάνω" seem to have the same suffix with the verbal forms of the first, singular person of the present tense of the active voice. For this reason, it is appropriate to know the part of speech of the word in order to find the stem as in the certain case the suffix of the verb is actually "-ω", while the numerals and adverbs are non declinable parts of speech and as a consequence their stem is the word itself.


Examples
-------

| WORD | CONFUSED WITH THE STEM OF ANOTHER POS | REAL STEM |
|------|---------------------------------------|-----------|
| εργαζόμενος (employee) | εργαζόμεν (confused with the stem of the adjectives) | εργαζ |
| οκτώ (eight) | οκτ (confused with the stem of the verbs) | οκτώ |
| παραπάνω (more) | παραπάν (confused with the stem of the verbs) | παραπάνω |


Install
-------

The recommended installation is via `pip`:

Simply type:
```shell script
$ pip install greek-stemmer-pos
```

Usage
-----

```python
from greek_stemmer import stemmer

stemmer.stem_word('εργαζόμενος', 'VBG')
// ΕΡΓΑΖ
```

How to contribute
-----------------
If you wish to contribute, you can start from [here](CONTRIBUTING.md) !

Run Test
----
- You can run the available tests with [pytest](https://docs.pytest.org/en/latest/)
- There are 149 available unittests

Code coverage
----
- Code coverage metrics are also available via [pytest-cov](https://github.com/pytest-dev/pytest-cov).
- Existing code coverage --> 100%

Python Package Index (PyPI)
----
- Library is available [here](https://pypi.org/project/greek-stemmer-pos/)