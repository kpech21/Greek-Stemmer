from ..closets.POS import pos_tags
from ..closets.rules import rules
from ..closets.word_exceptions import exceptions


def stem(word: str, pos: str) -> str:
    """Stem method responsible to apply lemmatization in a given verb

    Args:
        word (str): The word to stem.
        pos (str): The POS of the given word.

    Returns:
        str: Return the lemmatized word
    """
    # rule-set 1Α: unlemmatized words
    # rule-set 1B: unlemmatized words
    # rule-set 1C: Numbers
    if pos in pos_tags['articles'] or word in exceptions['unlemmatized'] + exceptions['numbers']:
        return word

    # rule-set 1D: ΕΝΔΟΝ, have always the lemma 'endon'
    elif word in exceptions['lemma_endon']:
        return 'ΕΝΔΟΝ'

    # rule-set 1E: ΠΛΗΣΙΟΝ, have always the lemma 'plision'
    elif word in exceptions['lemma_plision']:
        return 'ΠΛΗΣΙΟΝ'

    # rule-set 1F: ΠΡΟΤΙΜΩ, have always the lemma 'protimo'
    elif word in exceptions['lemma_protimo']:
        return 'ΠΡΟΤΙΜΩ'

    # rule-set 1G: noun with extra sigma
    elif word in exceptions['extra_sigma']:
        return word[:-1]

    # rule-set 2: neuter noun with suffix ΜΑΤΟΣ, ΜΑΤΑ, ΜΑΤΩΝ, ΜΑ
    if pos in ['NNN', 'NNSN', 'NNPN', 'NNPSN']:

        for suffix in rules['non_verbs']['neuter_noun']['matos']:

            if word.endswith(suffix):
                return word[:len(word) - len(suffix)] + 'Μ'

    # rule-set 3: suffix for propernames
    if pos in pos_tags['nouns']['singular']['propername'] + pos_tags['nouns']['plural']['propername']:

        for suffix in rules['non_verbs']['propername']:

            if word.endswith(suffix):
                return word[:len(word) - len(suffix)]

    # rule-set 4: irregular adjectives
    for adjective in exceptions['irregular_adjective']:

        if word.startswith(adjective):

            for suffix in rules['non_verbs']['irregular_adjective']:

                if word.endswith(suffix):
                    return word[:len(word) - len(suffix)]

    # rule-set 5: Adjectives, Participles and Pronouns
    if pos in pos_tags['adjectives'] + pos_tags['participles'] + pos_tags['pronouns']:

        for suffix in rules['non_verbs']['adjectives']:

            if word.endswith(suffix):
                return word[:len(word) - len(suffix)]

    # rule-set 6: Singular Noun
    elif pos in pos_tags['nouns']['singular']['noun'] + pos_tags['nouns']['singular']['propername']:

        if pos in ['NNF', 'NNPF']:
            if word[-3:] in ['ΕΑΣ', 'ΙΑΣ'] and len(word[:-2]) > 1:
                return word[:-2]

        for suffix in rules['non_verbs']['singular_noun']:

            if word.endswith(suffix):
                return word[:len(word) - len(suffix)]

    # rule-set 7: Plural Noun
    elif pos in pos_tags['nouns']['plural']['noun'] + pos_tags['nouns']['plural']['propername']:

        for suffix in rules['non_verbs']['plural_noun']:

            if word.endswith(suffix):
                return word[:len(word) - len(suffix)]

    # rule-set 8: Adverb
    elif pos == 'RB':

        for suffix in rules['non_verbs']['adverb']:

            if word.endswith(suffix):
                return word[:len(word) - len(suffix)]

    return word
