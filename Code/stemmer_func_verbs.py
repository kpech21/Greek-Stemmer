# -*- coding: utf-8 -*-
#!/usr/bin/python

#	stemmer_verb_gr.py is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    stemmer_verb_gr.py is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Foobar.  If not, see <http://www.gnu.org/licenses/>.

#############################################################################################################
#																											#
# 	AUTHOR	: Konstantinos Pechlivanis & Eirini Florou 					        							#
#																											#
#	LAST MOD: 14/01/2015																					#
#																											#
#	SUMMARY : this funtion finds the lemma of words (only for verbs), function "stem" estimates the lemma 	#
#			  and function "ends_with" estimates the suffix													#
#																											#
#	OUTPUS	: return the lemma of word																		#
#																					  						#
#############################################################################################################

vowels = ['Α', 'Ε', 'Η', 'Ι', 'Ο', 'Υ', 'Ω', 'Ά', 'Έ', 'Ή', 'Ί', 'Ό', 'Ύ', 'Ώ', 'Ϊ', 'Ϋ']

def ends_with(word, suffix):
    return word[len(word) - len(suffix):] == suffix

def stem(word, typePOS):

    #print 'Type of verb ' + word + '-->' + typePOS

######rule-set 1 --- Specific verbs
    if word in ['ΕΙΜΑΙ', 'ΕΙΣΑΙ', 'ΕΙΝΑΙ', 'ΕΙΜΑΣΤΕ' , 'ΕΙΣΤΕ', 'ΕΙΣΑΣΤΕ'] :
        return 'ΕΙ'
    elif word in ['ΗΜΟΥΝ', 'ΗΣΟΥΝ', 'ΗΤΑΝΕ', 'ΗΜΟΥΝΑ', 'ΗΣΟΥΝΑ', 'ΗΜΑΣΤΕ', 'ΗΣΑΣΤΕ', 'ΗΜΑΣΤΑΝ', 'ΗΣΑΣΤΑΝ', 'ΗΤΑΝ']:
        return 'Η'
    elif word in ['ΔΩ', 'ΔΕΙΣ', 'ΔΕΙ', 'ΔΟΥΜΕ', 'ΔΕΙΤΕ', 'ΔΟΥΝ', 'ΠΩ', 'ΠΕΙΣ', 'ΠΕΙ', 'ΠΟΥΜΕ', 'ΠΕΙΤΕ', 'ΠΟΥΝ', 'ΖΩ', 'ΖΕΙΣ', 'ΖΕΙ', 'ΖΟΥΜΕ', 'ΖΕΙΤΕ', 'ΖΟΥΝ', 'ΖΟΥΝΕ', 'ΖΟΥΣΑ', 'ΖΟΥΣΕΣ', 'ΖΟΥΣΕ', 'ΖΟΥΣΑΜΕ', 'ΖΟΥΣΑΤΕ', 'ΖΟΥΣΑΝΕ', 'ΖΟΥΣΑΝ'] :
		return word.decode('utf-8')[0]

######rule-set 2 --- ACTIVE VOICE, Singular --- PASSIVE VOICE, Singular
    if typePOS in ['VB', 'VBD', 'VBF', 'MD']:
        for suffix in ['ΙΟΜΟΥΝΑ', 'ΙΟΣΟΥΝΑ', 'ΟΥΜΟΥΝΑ', 'ΟΥΣΟΥΝΑ']:
            if ends_with(word, suffix):
				if (len(word.decode('utf-8')) - len(suffix.decode('utf-8'))) >1:
					return word[:len(word) - len(suffix)]
        for suffix in ['ΙΟΜΟΥΝ', 'ΙΟΣΟΥΝ', 'ΙΟΤΑΝΕ', 'ΟΥΣΟΥΝ', 'ΟΥΜΟΥΝ','ΟΜΟΥΝΑ', 'ΟΣΟΥΝΑ', 'ΑΡΗΣΕΣ'] :
            if ends_with(word, suffix):
               if (len(word.decode('utf-8')) - len(suffix.decode('utf-8'))) >1:
					return word[:len(word) - len(suffix)]
        for suffix in ['ΩΝΤΑΣ', 'ΟΝΤΑΣ', 'ΟΜΟΥΝ', 'ΟΣΟΥΝ', 'ΟΤΑΝΕ', 'ΟΥΣΑΙ', 'ΟΥΤΑΙ', 'ΟΥΣΕΣ', 'ΑΡΕΙΣ', 'ΙΕΜΑΙ', 'ΙΕΣΑΙ', 'ΙΕΤΑΙ', 'ΟΥΜΑΙ',
                       'ΕΙΣΑΙ', 'ΕΙΤΑΙ', 'ΙΟΤΑΝ', 'ΑΡΗΣΕ', 'ΑΡΗΣΑ']:
            if suffix == 'ΙΟΤΑΝ' and (len(word.decode('utf-8'))>5):
                if (word.decode('utf-8')[-6] in vowels):
                    continue
            if ends_with(word, suffix):
                if (len(word.decode('utf-8')) - len(suffix.decode('utf-8'))) > 1:
					return word[:len(word) - len(suffix)]
        for suffix in ['ΕΣΑΙ', 'ΕΤΑΙ', 'ΗΚΕΣ', 'ΟΜΑΙ', 'ΟΤΑΝ', 'ΟΥΣΑ',  'ΟΥΣΕ', 'ΑΓΕΣ', 'ΩΜΑΙ', 'ΑΣΑΙ', 'ΑΤΑΙ', 'ΑΡΕΣ', 'ΑΡΕΙ'] :
            if ends_with(word, suffix):
                if (len(word.decode('utf-8')) - len(suffix.decode('utf-8'))) > 1:
					return word[:len(word) - len(suffix)]
        for suffix in ['ΜΑΙ', 'ΣΑΙ', 'ΤΑΙ', 'ΜΗΝ', 'ΗΚΑ', 'ΗΚΕ', 'ΕΙΣ', 'ΑΕΙ','ΑΓΑ', 'ΑΓΕ', 'ΟΙΣ', 'ΑΡΩ', 'ΑΡΑ', 'ΑΡΕ'] :
            if ends_with(word, suffix):
                if (len(word.decode('utf-8')) - len(suffix.decode('utf-8'))) > 1:
					return word[:len(word) - len(suffix)]
        for suffix in ['ΟΥ', 'ΗΝ', 'ΗΣ',  'ΕΙ', 'ΑΩ', 'ΑΣ', 'ΕΣ', 'ΟΙ', 'ΣΟ', 'ΤΟ']:
            if ends_with(word, suffix):
                if (len(word.decode('utf-8')) - len(suffix.decode('utf-8'))) > 1:
					return word[:len(word) - len(suffix)]
        for suffix in ['Ω', 'Α', 'Ε', 'Η']:
            if ends_with(word, suffix):
                if (len(word.decode('utf-8')) - len(suffix.decode('utf-8'))) > 1:
					return word[:len(word) - len(suffix)]

######rule-set 3 --- ACTIVE VOICE, Plural --- PASSIVE VOICE, Plural
    elif typePOS in ['VBS', 'VBDS', 'VBFS']:
        for suffix in ['ΙΟΝΤΟΥΣΑΝ', 'ΙΟΜΑΣΤΑΝ', 'ΙΟΣΑΣΤΑΝ', 'ΙΟΥΝΤΑΝΕ', 'ΟΥΜΑΣΤΑΝ', 'ΟΥΣΑΣΤΑΝ']:
            if ends_with(word, suffix):
                if (len(word.decode('utf-8')) - len(suffix.decode('utf-8'))) > 1:
					return word[:len(word) - len(suffix)]
        for suffix in ['ΟΝΤΟΥΣΑΝ', 'ΟΜΑΣΤΑΝ', 'ΟΥΝΤΑΝΕ', 'ΟΣΑΣΤΑΝ', 'ΑΡΗΣΑΜΕ', 'ΑΡΗΣΑΤΕ', 'ΙΟΜΑΣΤΕ', 'ΙΟΣΑΣΤΕ', 'ΙΟΥΝΤΑΙ', 'ΟΥΜΑΣΤΕ', 'ΙΟΝΤΑΝΕ', 'ΙΟΥΝΤΑΝ'] :
            if (suffix in ['ΙΟΥΝΤΑΙ', 'ΙΟΥΝΤΑΝ']) and (len(word.decode('utf-8'))>7) :
                if word.decode('utf-8')[-8] in vowels :
                    continue
            if ends_with(word, suffix):
				if (len(word.decode('utf-8')) - len(suffix.decode('utf-8'))) > 1:
					return word[:len(word) - len(suffix)]
        for suffix in ['ΟΥΝΤΑΝ', 'ΙΟΝΤΑΝ', 'ΟΝΤΑΝΕ', 'ΟΥΝΤΑΙ', 'ΟΣΑΣΤΕ', 'ΟΜΑΣΤΕ', 'ΟΥΣΑΜΕ', 'ΟΥΣΑΤΕ','ΟΥΣΑΝΕ', 'ΟΥΜΕΘΑ', 'ΑΡΟΥΜΕ','ΙΟΝΤΑΙ',
                       'ΑΡΗΣΑΝ', 'ΟΣΑΣΤΕ'] :
            if ends_with(word, suffix):
                if (len(word.decode('utf-8')) - len(suffix.decode('utf-8'))) > 1:
					return word[:len(word) - len(suffix)]
        for suffix in ['ΑΓΑΜΕ', 'ΑΓΑΤΕ', 'ΟΥΣΘΕ', 'ΩΜΕΘΑ', 'ΑΡΕΤΕ', 'ΑΡΟΥΝ', 'ΩΝΤΑΣ', 'ΩΝΤΑΙ', 'ΑΡΑΜΕ', 'ΑΡΑΤΕ', 'ΑΡΑΝΕ', 'ΟΝΤΑΣ', 'ΗΚΑΜΕ',
                       'ΕΙΣΤΕ', 'ΟΝΤΑΙ', 'ΗΚΑΤΕ', 'ΗΚΑΝΕ', 'ΑΓΑΝΕ', 'ΟΝΤΑΝ', 'ΙΕΣΤΕ', 'ΟΥΤΑΝ', 'ΟΥΣΙΝ'] :
			if ends_with(word, suffix):
				if (len(word.decode('utf-8')) - len(suffix.decode('utf-8'))) > 1:
					return word[:len(word) - len(suffix)]
        for suffix in ['ΟΥΣΑΝ', 'ΟΥΤΕ', 'ΜΕΘΑ', 'ΝΤΑΙ', 'ΗΜΕΝ', 'ΗΣΕΝ', 'ΗΣΑΝ', 'ΗΚΑΝ', 'ΟΥΜΕ', 'ΟΥΝΕ', 'ΕΙΤΕ', 'ΑΣΘΕ', 'ΑΓΑΝ', 'ΕΣΤΕ', 'ΑΡΑΝ', 'ΩΜΕΝ', 'ΟΥΣΙ'] :
			if ends_with(word, suffix):
				if (len(word.decode('utf-8')) - len(suffix.decode('utf-8'))) > 1:
					return word[:len(word) - len(suffix)]
        for suffix in ['ΟΜΕ', 'ΕΤΕ', 'ΑΜΕ', 'ΑΤΕ', 'ΑΝΕ', 'ΟΥΝ', 'ΗΤΕ', 'ΣΘΕ', 'ΝΤΟ']:
			if ends_with(word, suffix):
				if (len(word.decode('utf-8')) - len(suffix.decode('utf-8'))) > 1:
					return word[:len(word) - len(suffix)]
        for suffix in ['ΑΝ', 'ΤΕ']:
			if ends_with(word, suffix):
				if (len(word.decode('utf-8')) - len(suffix.decode('utf-8'))) > 1:
					return word[:len(word) - len(suffix)]

    return word
