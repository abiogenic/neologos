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

import unicodedata

#===================================================================================#
#===================================DEFNITIONS======================================#
#===================================================================================#

import pandas as pd
import numpy as np
from functions import *
from classes import *
from global_settings import *

low_to_high = ['open','near-open','open-mid','mid','close-mid','near-close','close']
front_to_back = ['front','near-front','central','near-back','back']
sonorous_to_non = ['vowel','glide','liquid','nasal','obstruent']

def find_diacritics(string):
	unicode_letters = []
	unicode_diacritics = []

	for key in range(0,len(sample_string)):
		i = sample_string[key]
		if 'COMBINING' in unicodedata.name(i) or 'MODIFIER' in unicodedata.name(i) or 'SUPERSCRIPT' in unicodedata.name(i) or 'SUBSCRIPT' in unicodedata.name(i):
			unicode_diacritics.append(i)
		elif i.isalpha():
			if i not in unicode_letters:
				unicode_letters.append(i)
		else:
			if i not in unicode_letters:
				unicode_diacritics.append(i)

	unicode_letters = list(set(unicode_letters))
	unicode_diacritics = list(set(unicode_diacritics))
	
	with open('letters_and_diacritics.csv', 'w', newline='', encoding='utf-8') as f:
		writer = csv.writer(f)
		writer.writerows(unicode_letters)
		writer.writerow("=====================")
		writer.writerows(unicode_diacritics)

	return(unicode_letters,unicode_diacritics)

def get_consonant(phone_attributes):
	query = ipa
	query = query[query['voicing'] == phone_attributes[2]]
	query = query[query['subplace'] == phone_attributes[4]]
	query = query[query['submanner'] == phone_attributes[6]]
	try:
		return(query.index[0])
	except:
		pass

def get_vowel(phone_attributes):
	query = ipa
	query = query[query['roundedness'] == phone_attributes[11]]
	query = query[query['height'] == phone_attributes[12]]
	query = query[query['backness'] == phone_attributes[13]]
	try:
		return(query.index[0])
	except:
		pass

def change_phone(phone,change_attr,change_to):
	x = copy.deepcopy(Phone(phone))
	x.dictionary[change_attr] = change_to
	phone_attributes = list()
	for key in x.dictionary.keys():
		phone_attributes.append(x.dictionary[key])
	if ipa_dict[phone].type == 'vowel':
		changed_phone = get_vowel(phone_attributes)
	elif ipa_dict[phone].type == 'consonant':
		changed_phone = get_consonant(phone_attributes)
	return(changed_phone)

#===================================================================================#
#==================================VOWEL FUNCTIONS==================================#
#===================================================================================#

def raise_vowel(vowel):
	cycle = True
	scale = 1
	while cycle:
		height_index = low_to_high.index(Phone(vowel).height)
		if height_index == len(low_to_high)-1:
			#cannot make vowel higher
			return(vowel)
		else:
			try:
				to_height = low_to_high[height_index+scale]
			except:
				return(vowel)
			new_vowel = change_phone(vowel,'height',to_height)
			if new_vowel == None:
				scale = scale+1
			else:
				cycle = False
	return(new_vowel)

def lower_vowel(vowel):
	cycle = True
	scale = 1
	while cycle:
		height_index = low_to_high.index(Phone(vowel).height)
		if height_index == 0:
			#cannot make vowel lower
			return(vowel)
		else:
			try:
				to_height = low_to_high[height_index-scale]
			except:
				return(vowel)
			new_vowel = change_phone(vowel,'height',to_height)
			if new_vowel == None:
				scale = scale+1
			else:
				cycle = False
	return(new_vowel)

def round_vowel(vowel):
	if Phone(vowel).roundedness == 'rounded':
		return(vowel)
	else:
		new_vowel = change_phone(vowel,'roundedness','rounded')
		if new_vowel == None:
			return(vowel)
		else:
			return(new_vowel)

def unround_vowel(vowel):
	if Phone(vowel).roundedness == 'unrounded':
		return(vowel)
	else:
		new_vowel = change_phone(vowel,'roundedness','unrounded')
		if new_vowel == None:
			return(vowel)
		else:
			return(new_vowel)

def push_vowel(vowel):
	cycle = True
	scale = 1
	while cycle:
		backness_index = front_to_back.index(Phone(vowel).backness)
		if backness_index == len(low_to_high)-1:
			#cannot push vowel further
			return(vowel)
		else:
			try:
				to_distance = low_to_high[backness_index+scale]
			except:
				return(vowel)
			new_vowel = change_phone(vowel,'backness',to_distance)
			if new_vowel == None:
				scale = scale+1
			else:
				cycle = False
	return(new_vowel)

def pull_vowel(vowel):
	cycle = True
	scale = 1
	while cycle:
		backness_index = front_to_back.index(Phone(vowel).backness)
		if backness_index == 0:
			#cannot pull vowel further
			return(vowel)
		else:
			try:
				to_distance = low_to_high[backness_index-scale]
			except:
				return(vowel)
			new_vowel = change_phone(vowel,'backness',to_distance)
			if new_vowel == None:
				scale = scale+1
			else:
				cycle = False
	return(new_vowel)

#===================================================================================#
#===============================CONSONANT FUNCTIONS=================================#
#===================================================================================#

def devoice(consonant):
	new_consonant = change_phone(consonant,'voicing','voiceless')
	if new_consonant != None:
		return(new_consonant)
	else:
		return(consonant)

def voice(consonant):
	new_consonant = change_phone(consonant,'voicing','voiced')
	if new_consonant != None:
		return(new_consonant)
	else:
		return(consonant)

def deaffricate(consonant):
	if Phone(consonant).manner == 'affricate':
		new_consonant = change_phone(consonant,'manner','fricative')
		if new_consonant != None:
			return(new_consonant)
		else:
			return(consonant)
	return(consonant)

#===================================================================================#
#===================================PHONE LISTS=====================================#
#===================================================================================#

vowels = list(ipa.loc[ipa.iloc[:]['type']=='vowel'][:].index)
consonants = list(ipa.loc[ipa.iloc[:]['type']=='consonant'][:].index)
diacritics = list(ipa.loc[ipa.iloc[:]['type']=='diacritic'][:].index)
stresses = list(ipa.loc[ipa.iloc[:]['type']=='stress'][:].index)
suprasegmentals = list(ipa.loc[ipa.iloc[:]['type']=='suprasegmental'][:].index)

voiced = list(ipa.loc[ipa.iloc[:]['voicing']=='voiced'][:].index)
voiceless = list(ipa.loc[ipa.iloc[:]['voicing']=='voiceless'][:].index)

coronals = list(ipa.loc[ipa.iloc[:]['place']=='coronal'][:].index)
dorsals = list(ipa.loc[ipa.iloc[:]['place']=='dorsal'][:].index)
labials = list(ipa.loc[ipa.iloc[:]['place']=='labial'][:].index)
laryengeals = list(ipa.loc[ipa.iloc[:]['place']=='laryengeal'][:].index)

labiodentals = list(ipa.loc[ipa.iloc[:]['subplace']=='labio-dental'][:].index)
pharyngeals = list(ipa.loc[ipa.iloc[:]['subplace']=='pharyngeal'][:].index)
glottals = list(ipa.loc[ipa.iloc[:]['subplace']=='glottal'][:].index)
alveolars = list(ipa.loc[ipa.iloc[:]['subplace']=='alveolar'][:].index)
retroflexes = list(ipa.loc[ipa.iloc[:]['subplace']=='retroflex'][:].index)
alveolars = list(ipa.loc[ipa.iloc[:]['subplace']=='alveolar'][:].index)
dentals = list(ipa.loc[ipa.iloc[:]['subplace']=='dental'][:].index)
palatoalveolars = list(ipa.loc[ipa.iloc[:]['subplace']=='palato-alveolar'][:].index)
uvulars = list(ipa.loc[ipa.iloc[:]['subplace']=='uvular'][:].index)
velars = list(ipa.loc[ipa.iloc[:]['subplace']=='velar'][:].index)
bilabials = list(ipa.loc[ipa.iloc[:]['subplace']=='bilabial'][:].index)

obstruents = list(ipa.loc[ipa.iloc[:]['manner']=='obstruent'][:].index)
sonorants = list(ipa.loc[ipa.iloc[:]['manner']=='sonorant'][:].index)

affricates = list(ipa.loc[ipa.iloc[:]['submanner']=='affricate'][:].index)
flaps = list(ipa.loc[ipa.iloc[:]['submanner']=='flap'][:].index)
trills = list(ipa.loc[ipa.iloc[:]['submanner']=='trill'][:].index)
nasals = list(ipa.loc[ipa.iloc[:]['submanner']=='nasal'][:].index)
fricatives = list(ipa.loc[ipa.iloc[:]['submanner']=='fricative'][:].index)
plosives = list(ipa.loc[ipa.iloc[:]['submanner']=='plosive'][:].index)
approximants = list(ipa.loc[ipa.iloc[:]['submanner']=='approximant'][:].index)

laterals = list(ipa.loc[ipa.iloc[:]['laterality']=='lateral'][:].index)
liquids = list(ipa.loc[ipa.iloc[:]['liquidity']=='liquid'][:].index)
stridents = list(ipa.loc[ipa.iloc[:]['stridency']=='strident'][:].index)
sibilants = list(ipa.loc[ipa.iloc[:]['sibilance']=='sibilant'][:].index)

unrounded_vowels = list(ipa.loc[ipa.iloc[:]['roundedness']=='unrounded'][:].index)
rounded_vowels = list(ipa.loc[ipa.iloc[:]['roundedness']=='rounded'][:].index)

close_vowels = list(ipa.loc[ipa.iloc[:]['height']=='close'][:].index)
close_mid_vowels = list(ipa.loc[ipa.iloc[:]['height']=='close-mid'][:].index)
mid_vowels = list(ipa.loc[ipa.iloc[:]['height']=='mid'][:].index)
near_close_vowels = list(ipa.loc[ipa.iloc[:]['height']=='near-close'][:].index)
near_open_vowels = list(ipa.loc[ipa.iloc[:]['height']=='near-open'][:].index)
open_vowels = list(ipa.loc[ipa.iloc[:]['height']=='open'][:].index)
open_mid_vowels = list(ipa.loc[ipa.iloc[:]['height']=='open-mid'][:].index)

back = list(ipa.loc[ipa.iloc[:]['backness']=='back'][:].index)
central = list(ipa.loc[ipa.iloc[:]['backness']=='central'][:].index)
front = list(ipa.loc[ipa.iloc[:]['backness']=='front'][:].index)



