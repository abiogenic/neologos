#!/usr/bin/env python3
# coding: utf-8
# dependences: none

#===================================================================================#
#=====================================SETTINGS======================================#
#===================================================================================#

import itertools
import random as rand
from classes import *

def insert_sound(word,sound,index_l,index_r = 'none'):
	if index_l > 0:
		lower_bound = sorted(word.dict_stripped.keys())[index_l]
		new_key = rand.uniform(lower_bound,lower_bound+1)
		word.dict[new_key] = sound
		word = repair_word(word)
		return(word)
	else:
		#lower_bound = sorted(word.dict_stripped.keys())[index_l]
		upper_bound = sorted(word.dict_stripped.keys())[index_l]
		new_key = rand.uniform(upper_bound-1,upper_bound)
		word.dict[new_key] = sound
		word = repair_word(word)
		return(word)

def initial(word,l1,c1='none'):
# 	Prothesis						tata > atata		insertion of initial sound
	if c1 == 'none':
		if l1 != word.string_stripped[0]:
			word = insert_sound(word,l1,0,0)
			return(word,1)
	else:
		if word.string_stripped[1] in c1:
			if l1 != word.string_stripped[0]:
				word = insert_sound(word,l1,0,0)
				return(word,1)
	return(word,0)

def medial(word,c1,l1,c2,conditions = 'none'):
# 	Anaptyxis (Parasitic Phone)		atta > atata		insertion of vowel between consonants
# 	Excrescence											amra > ambra; anra > andra; ansa > antsa
	for x in itertools.product(c1, c2):
		if str(x[0]+x[1]) in word.string_stripped:
			query = word.string_stripped
			query = query.split(str(x[0]+x[1]))
			output = str()
			for i in range(0,len(query)):
				if i == len(query)-1:
					output = output + query[i]
				else:
					output = output + query[i] + str(x[0]) + str(l1) + str(x[1])
			print(output)
			word = Word(tokenize_word(output))
			return(word, 1)
	return(word, 0)

def final(word,l1,c1='none'):
# 	Paragoge						tat > tata			insertion of final sound (mostly vowels)
	if c1 == 'none':
		if l1 != word.string_stripped[-1]:
			i = len(word.string_stripped)
			word = insert_sound(word,l1,i-1)
			return(word,1)
	else:
		if word.string_stripped[-1] in c1:
			if l1 != word.string_stripped[-1]:
				i = len(word.string_stripped)
				word = insert_sound(word,l1,i-1)
				return(word,1)
	return(word,0)