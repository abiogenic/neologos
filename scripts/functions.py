#!/usr/bin/env python3
# coding: utf-8
# dependences: pandas, numpy

#===================================================================================#
#=================================IMPORT MODULES====================================#
#===================================================================================#

import random as rand
import time
import sys
import copy
import csv
import os
import glob
import shutil
from datetime import datetime, timedelta
from operator import *

#===================================================================================#
#==================================DEPENDENCIES=====================================#
#===================================================================================#

import pandas as pd
import numpy as np
import sounds
from sounds import *
from classes import *
from global_settings import *

#===================================================================================#
#=====================================CLASSES=======================================#
#===================================================================================#

def repair_word(word):
	repaired_word = str()
	for key in sorted(word.dict.keys()):
		repaired_word = repaired_word + str(word.dict[key])
	repaired_word = repaired_word[1:-1]
	word = Word(tokenize_word(repaired_word))
	return(word)

def tokenize_word(string):
	V = 'V'
	C = 'C'
	E = '/'
	D = '*'
	Onset = 'Onset'
	Coda = 'Coda'
	S = 'S'
	string_stripped = str()
	print("string: ", string)
	#print([str(element) for element in string])
	for element in string:
		if element in sounds.stresses:
			pass
		else:
			string_stripped = string_stripped + str(element)	

	dict_stripped = {i:string_stripped[i] for i in range(0,len(string_stripped))}

	new_dict = []
	new_string = str()
	for key in sorted(dict_stripped.keys()):
		new_dict.append(dict_stripped[key])
		new_string = new_string + dict_stripped[key]
	new_dict = {i:new_dict[i] for i in range(0,len(new_dict))}

	### final codas are still syllabified as onsets
	temp_string = str()

	for i in new_string:
		if i in sounds.suprasegmentals:
			temp_string = temp_string + "."
		else:
			temp_string = temp_string + i

	new_string = temp_string
	print("string tokenization: \t", new_string)
	syllables = new_string.split('.')
	
	new_string = str()
	for syllable in syllables:
		syllable_string = str()
		vowel_count = 0
		keys = []
		syllable_dict = {i:syllable[i] for i in range(0,len(syllable))}
		for key in range(0,len(syllable)):
			l = syllable[key]
			if l in sounds.vowels:
				keys.append(key)
				vowel_count = vowel_count + 1
		if vowel_count > 1:
			for key in keys[:-1]:
				new_key = rand.uniform(key,key+1)
				syllable_dict[new_key] = "."
				#print(syllable_dict)
		syllable_keys = sorted(syllable_dict)
		for key in syllable_keys:
			syllable_string = syllable_string + syllable_dict[key]
		new_string = new_string + syllable_string + "."



	new_string = new_string.strip('.')
	print("syllable tokenization: \t", new_string)
	syllables = new_string.split('.')
	
	syllable_len = len(syllables)
	feet_locations = [i*foot_max for i in range(0,int(syllable_len/foot_max))]
	# ODD: feet should be at 1,3,5,... to syllable_len-2
	if syllable_len < foot_max:
		if build_feet == 'l':
			feet_locations = [0]
		elif build_feet == 'r':
			feet_locations = [-1]
	elif syllable_len % foot_max != 0:
		if build_feet == 'l':
			feet_locations = [i for i in feet_locations]
		elif build_feet == 'r':
			feet_locations = [i+1 for i in feet_locations]
	
	if stress_feet == 'l':
		main_stress = feet_locations
	elif stress_feet == 'r':
		feet_locations = [i+foot_max-1 for i in feet_locations]
		main_stress = feet_locations

	new_word = str()

	for j in range(0,syllable_len):

		new_foot = 0

		if j in feet_locations and j != 0:
			new_foot = 1


			#""" find primary stress """
		if main_stressed_foot == 'r':
			stressed_foot = main_stress[-1]
		elif main_stressed_foot == 'l':
			stressed_foot = main_stress[0]
		elif type(main_stressed_foot) == int:
			stressed_foot = main_stress[main_stressed_foot]
		
		#""" mark primary and secondary stress """
		if j == stressed_foot:
			s = str("ˈ") + syllables[j]
		elif j in main_stress:
			s = str("ˌ") + syllables[j]
		else:
			s = syllables[j]

		#""" build syllable """
		if build_feet == 'l':
			if j in [i + foot_max -1 for i in main_stress]:
				new_word = new_word  + s + "|"
			else:
				new_word = new_word + s + "."
		elif build_feet == 'r':
			if j in main_stress:
				new_word = new_word + "|" + s
			else:
				new_word = new_word + "." + s

	new_string = new_word.strip('.')
	new_string = new_string.strip("|")

	print("stress tokenization: \t", new_string)
	return(new_string)

def insert_sound(word,sound,index_l,index_r = 'none'):
	if index_l > 0:
		lower_bound = sorted(word.dict_stripped.keys())[index_l]
		new_key = rand.uniform(lower_bound,lower_bound+1)
		word.dict[new_key] = sound
		word = repair_word(word)
		return(word)
	else:
		upper_bound = sorted(word.dict_stripped.keys())[index_l]
		new_key = rand.uniform(upper_bound-1,upper_bound)
		word.dict[new_key] = sound
		word = repair_word(word)
		return(word)

def change_sound(word,sound,index):
	word.dict[index] = sound
	word = repair_word(word)
	return(word)

# def delete_sound(word,index_l):
# 	del word.dict[index_l]
# 	new_word = str()
# 	for value in word.dict.values():
# 		new_word = new_word + value
# 	print(new_word)
# 	word = Word(tokenize_word(new_word))
# 	return(word)




