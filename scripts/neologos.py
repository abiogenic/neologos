#!/usr/bin python3.7
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
import string

import unicodedata

wd = os.getcwd()

print(sys.version)

#===================================================================================#
#==================================DEPENDENCIES=====================================#
#===================================================================================#

needs_dependency = False

try:
	import pandas as pd
except:
	print("Dependency not found: pandas")
	needs_dependency = True
try:
	import numpy as np
except:
	print("Dependency not found: numpy")
	needs_dependency = True

from sounds import *
from functions import *
from classes import *
from changes import *
from global_settings import *
 
if needs_dependency:
	quit()

#===================================================================================#
#==================================SETTINGS CHECK===================================#
#===================================================================================#

if fix_randomization:
	rand.seed(seed_variable)

if main_stressed_foot != 'r' and main_stressed_foot != 'l':
	if type(main_stressed_foot) != int:
		print("ERROR: Setting 'main_stressed_foot' is invalid.")
		quit()
if type(main_stressed_foot) == int:
	if main_stressed_foot > min_len/foot_max - 1:
		print("ERROR: Setting 'main_stressed_foot' is an invalid integer.")
		print("ERROR (cont.): 'main_stressed_foot' must be no greater than (min_len/foot-max)-1")
		print("ERROR (cont.): (min_len/foot-max)-1 = ", str(min_len/foot_max - 1))
		quit()
if min_len > max_len:
	print("ERROR: Settings 'min_len' is greater than 'max_len'.")
	print("ERROR (cont.): Can't do that, brah.")

#===================================================================================#
#==================================DIRECTORIES======================================#
#===================================================================================#

home_dir = str(os.getcwd() + "/..")
os.chdir(home_dir)

input_dir = home_dir + "/input"
output_dir = home_dir + "/output"
scripts_dir = home_dir + "/scripts"

day = datetime.now()
timestamp = str(day)
timestamp = timestamp.split()
current_date = timestamp[0]

#===================================================================================#
#=====================================FUNCTIONS=====================================#
#===================================================================================#

def create_words(file_name):

	output = []

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
		output.append([new_word])

	with open(file_name, 'w', newline='', encoding='utf-8') as f:
		writer = csv.writer(f)
		writer.writerows(output)

def check_words(file_name):
	with open(file_name, 'r', newline='', encoding='utf-8') as f:
		reader = csv.reader(f)
		unprocessed_words = [i[0] for i in reader]
		
	output = []

	for unprocessed_word in unprocessed_words:
		print("\n\n")
		
		print("=================================")
		word = Word(unprocessed_word)

		row = [word]

		print("original string: \t", word.string)
		print("original string_s: \t",word.string_stripped)

		for i in range(0,1):

			word = phone_rasing(word)
			word = phone_lowering(word)

			print("new string: \t\t", word.string)
			print("new string_s: \t\t",word.string_stripped)
			row.append(word)
			
		output.append(row)

	with open(file_name, 'w', newline='', encoding='utf-8') as f:
		writer = csv.writer(f)
		writer.writerows(output)

#===================================================================================#
#==================================FUNCTION CALLS===================================#
#===================================================================================#

def find_diacritics(string):
	letters = []
	diacritics = []

	for key in range(0,len(sample_string)):
		i = sample_string[key]
		if 'COMBINING' in unicodedata.name(i) or 'MODIFIER' in unicodedata.name(i) or 'SUPERSCRIPT' in unicodedata.name(i) or 'SUBSCRIPT' in unicodedata.name(i):
			diacritics.append(i)
		elif i.isalpha():
			print(i)
			if i not in letters:
				letters.append(i)
		elif i == ".":
			pass
		elif i.isspace():
			pass
		else:
			if i not in letters:
				print(i)
				diacritics.append(i)


	letters = list(set(letters))
	diacritics = list(set(diacritics))
	

	with open('letters_and_diacritics.csv', 'w', newline='', encoding='utf-8') as f:
		writer = csv.writer(f)
		writer.writerows(letters)
		writer.writerow("=====================")
		writer.writerows(diacritics)

	return(letters,diacritics)

letters,diacritics = find_diacritics(sample_string)


print(letters)

print("=====")

print(diacritics)

# u = chr(233) + chr(0x0bf2) + chr(3972) + chr(6000) + chr(13231)

# for i, c in enumerate(u):
#     print(i, '%04x' % ord(c), unicodedata.category(c), end=" ")
#     print(unicodedata.name(c))

# # Get numeric value of second character
# print(unicodedata.numeric(u[1]))


quit()

os.chdir(output_dir)

create_words(file_name)

check_words(file_name)


