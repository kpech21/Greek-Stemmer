# -*- coding: utf-8 -*-
#!/usr/bin/python

import os, sys, unicodedata	# import libraries
import stemmer_func, stemmer_func_verbs

reload(sys)
sys.setdefaultencoding('utf-8')

word= str(sys.argv[1])
POS = str(sys.argv[2])

# Remove accents - Upper case
word = word.decode('utf-8').upper().encode('utf-8')
nkfd_form = unicodedata.normalize('NFKD', unicode(word))
word = "".join([c for c in nkfd_form if not unicodedata.combining(c)])
word = word.decode('utf-8').upper().encode('utf-8')


if POS in ['VB', 'VBD', 'VBF', 'MD', 'VBS', 'VBDS', 'VBFS'] : # if word is verb or modal verb
	word = stemmer_func_verbs.stem(word, POS)
elif POS=='FW':
	print 'Non-Greek word'
else:
	word = stemmer_func.stem(word, POS)
word = word.decode('utf-8')

print word
