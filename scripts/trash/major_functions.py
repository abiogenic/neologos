#!/usr/bin python3.7
# coding: utf-8
# dependences: pandas, numpy

#===================================================================================#
#=================================IMPORT MODULES====================================#
#===================================================================================#

import random as rand
import os
import unicodedata

#===================================================================================#
#==================================DEPENDENCIES=====================================#
#===================================================================================#

from sounds import *
# from functions import *
from classes import *
from changes import *
from global_settings import *

#===================================================================================#
#=====================================FUNCTIONS=====================================#
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
	
def create_words():

	data = []

	for i in range(0,words_to_create):

	#""" word creation """

		new_word = str()
		syllable_len = rand.randint(min_len,max_len)

		# EVEN: feet should be at 0,2,4,... to syllable_len-2
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

		for j in range(0,syllable_len):

			new_foot = 0

			if j in feet_locations and j != 0:
				new_foot = 1

			#""" syllable creation """

			onset = str()
			nucleus = str()
			coda = str()

			#""" if nucleus is a syllabic_consonant """
			if rand.random() <= syllabic_consonant_freq:
				nucleus = str(rand.sample(syllabic_consonants,1)[0])
			
			#""" if nucleus is not a syllabic_consonant """
			else:

				#""" create onset """
				if rand.random() <= complex_onsets_freq:
					onset = rand.sample(complex_onsets,1)[0]
				else:
					onset = rand.sample(onsets,1)[0]

				#""" create nucleus """
				if rand.random() <= complex_nucleus_freq:
					nucleus = rand.sample(diphthongs,1)[0]
				else:
					nucleus = rand.sample(nuclear_vowels,1)[0]

				#""" create coda """
				if rand.random() <= coda_frequency:
					coda = rand.sample(codas,1)[0]
			
			#""" find primary stress """
			if main_stressed_foot == 'r':
				stressed_foot = main_stress[-1]
			elif main_stressed_foot == 'l':
				stressed_foot = main_stress[0]
			elif type(main_stressed_foot) == int:
				stressed_foot = main_stress[main_stressed_foot]
			
			#""" mark primary and secondary stress """
			if j == stressed_foot:
				onset = str("ˈ") + onset
			elif j in main_stress:
				onset = str("ˌ") + onset

			#""" build syllable """
			if build_feet == 'l':
				if j in [i + foot_max -1 for i in main_stress]:
					new_word = new_word  + onset + nucleus + coda + "|"
				else:
					new_word = new_word + onset + nucleus + coda + "."
			elif build_feet == 'r':
				if j in main_stress:
					new_word = new_word + "|" + onset + nucleus + coda
				else:
					new_word = new_word + "." + onset + nucleus + coda


		new_word = new_word.strip(".")
		new_word = new_word.strip("|")
		x = Word(new_word)
		print("word\t", x.string)
		# print("feet\t", x.feet)
		# print("syllables\t", x.syllables)
		data.append([new_word])

	return(data)

def check_words(data):

	unprocessed_words = copy.deepcopy(data)

	data = []

	print(unprocessed_words)

	for word in [i[0] for i in unprocessed_words]:
		print("\n\n")
		print("=================================")
		word = Word(word)
		row = [str(word)]

		print("original string: \t", word.string)
		print("original string_s: \t",word.string_stripped)

		for i in range(0,1):

			#word = phone_rasing(word)
			word = phone_lowering(word)

			print("new string: \t\t", word.string)
			print("new string_s: \t\t",word.string_stripped)
			row.append(str(word))

			word = phone_lowering(word)

			
			print("new string: \t\t", word.string)
			print("new string_s: \t\t",word.string_stripped)
			row.append(str(word))
			
		data.append(row)

	return(data)

def write_file(data, file_name):

	with open(file_name, 'w', newline='', encoding='utf-8') as f:
		writer = csv.writer(f)
		writer.writerows(data)


