# all the available Part of Speech Tags

total_pos_tags = [
    'DDT', 'IDT', 'NNM', 'NNF', 'NNN', 'NNSM', 'NNSF', 'NNSN', 'NNPM', 'NNPF', 'NNPN', 'NNPSM', 'NNPSF', 'NNPSN', 'VB',
    'VBD', 'VBF', 'MD', 'VBS', 'VBDS', 'VBFS', 'JJM', 'JJF', 'JJN', 'JJSM', 'JJSF', 'JJSN', 'CD', 'VBG', 'VBP', 'VBPD',
    'PRP', 'PP', 'REP', 'DP', 'IP', 'WP', 'QP', 'INP', 'RB', 'IN', 'CC', 'RP', 'UH', 'FW', 'DATE', 'TIME', 'AB', 'SYM']

pos_tags = {
    'articles': [
        'DDT',
        'IDT'
    ],
    'nouns':
        {
            'singular': {
                'noun': ['NNM', 'NNF', 'NNN'],
                'propername': ['NNPM', 'NNPF', 'NNPN']
            },
            'plural': {
                'noun': ['NNSM', 'NNSF', 'NNSN'],
                'propername': ['NNPSM', 'NNPSF', 'NNPSN']
            }
        },
    'verbs':
        {
            'singular': ['VB', 'VBD', 'VBF', 'MD'],
            'plural': ['VBS', 'VBDS', 'VBFS']
        },
    'adjectives': [
        'JJM',
        'JJF',
        'JJN',
        'JJSM',
        'JJSF',
        'JJSN',
        'CD'
    ],
    'participles': [
        'VBG',
        'VBP',
        'VBPD'
    ],
    'pronouns': [
        'PRP',
        'PP',
        'REP',
        'DP',
        'IP',
        'WP',
        'QP',
        'INP'
    ],
    'others': [
        'RB',
        'IN',
        'CC',
        'RP',
        'UH',
        'FW',
        'DATE',
        'TIME',
        'AB',
        'SYM'
    ]
}
