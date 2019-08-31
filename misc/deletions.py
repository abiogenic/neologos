#!/usr/bin/env python3
# coding: utf-8
# dependences: none

#===================================================================================#
#=====================================SETTINGS======================================#
#===================================================================================#

import itertools
import random as rand
from classes import *

# def delete_sound(word,index_l):
# 	del word.dict[index_l]
# 	new_word = str()
# 	for value in word.dict.values():
# 		new_word = new_word + value
# 	print(new_word)
# 	word = Word(tokenize_word(new_word))
# 	return(word)

def initial(word,a1,c1='none'):
# 	Aphaeresis						atata > tata		deletion of initial sound (mostly vowels)	
	if c1 == 'none':
		for x in a1:
			if x == word.string_stripped[0]:
				i = sorted(word.dict_stripped.keys())[0]
				del word.dict[i]
				new_word = str()
				for value in word.dict.values():
					new_word = new_word + value
				print(new_word)
				word = Word(tokenize_word(new_word[1:-1]))
				return(word,1)
	else:
		if word.string_stripped[1] in c1:
			for x in a1:
				if x == word.string_stripped[0]:
					i = sorted(word.dict_stripped.keys())[0]
					del word.dict[i]
					new_word = str()
					for value in word.dict.values():
						new_word = new_word + value
					print(new_word)
					word = Word(tokenize_word(new_word[1:-1]))
					return(word,1)
	return(word,0)

def medial(word,c1,l1,c2,conditions = 'none'):
# 	Syncope							atata > atta		deletion from interior (mostly vowels)	
	for x in itertools.product(c1, l1, c2):
		if str(x[0]+x[1]+x[2]) in word.string_stripped:
			query = word.string_stripped.split(str(x[0]+x[1]+x[2]))
			output = str()
			for i in range(0,len(query)):
				if i == len(query)-1:
					output = output + query[i]
				else:
					output = output + query[i] + str(x[0]) + str(x[2])
			word = Word(tokenize_word(output))
			return(word,1)
	return(word,0)

def final(word,a1,c1='none'):
# 	Apocope							tato > tat			deletion from end of word	
	if c1 == 'none':
		for x in a1:
			if x == word.string_stripped[-1]:
				i = sorted(word.dict_stripped.keys())[-1]
				del word.dict[i]
				new_word = str()
				for value in word.dict.values():
					new_word = new_word + value
				print(new_word)
				word = Word(tokenize_word(new_word[1:-1]))
				return(word,1)
	else:
		if word.string_stripped[-2] in c1:
			for x in a1:
				if x == word.string_stripped[-1]:
					i = sorted(word.dict_stripped.keys())[-1]
					del word.dict[i]
					new_word = str()
					for value in word.dict.values():
						new_word = new_word + value
					print(new_word)
					word = Word(tokenize_word(new_word[1:-1]))
					return(word,1)
	return(word,0)