#!/usr/bin/env python3.7
# coding: utf-8
# dependences: none

#===================================================================================#
#=====================================SETTINGS======================================#
#===================================================================================#

import itertools
import random as rand
from classes import *
from sounds import *

def syncope(word):
# 	Syncope							atata > atta					deletion from interior (mostly vowels)
	return(word)

def apocope(word):
# 	Apocope							tato > tat						deletion from end of word
	return(word)

def aphaeresis(word):
# 	Aphaeresis						atata > tata					deletion of initial sound (mostly vowels)
	return(word)

def prothesis(word):
# 	Prothesis						tata > atata					insertion of initial sound
	return(word)

def prothesis(word):
# 	Anaptyxis (Parasitic Vowel)		atta > atata					insertion of vowel between consonants
	return(word)

def prothesis(word):
# 	Excrescence						amra > ambra; 					insertion of consonant between consonants
# 									anra > andra; 
#									ansa > antsa		
	return(word)

def prothesis(word):
# 	Paragoge						tat > tata						insertion of final sound (mostly vowels)
	return(word)		

def rhotacism(word):
# 	Rhotacism						VsV > VrV						/s/ or /z/ goes to /r/ usually between vowels or glides
	return(word)

def metathesis(word):
# 	Metathesis						asta > atsa, asata > atasa		sounds change positions (sometimes sporatically)
	return(word)

def breaking(word):
# 	Breaking						V > VV							diphthongization of a short vowel
	return(word)

def final_devoicing(word):
# 	Final Devoicing					tad > tat						word- or syllable-final sounds devoice
	return(word)

def intervocalic_voicing(word):		
# 	Intervocalic Voicing			ata > ada						voicing between vowels
	return(word)

def nasal_assimilation(word):
# 	Nasal assimilation				Np > mp							nasals agree in place with following sound
	return(word)

def palatalization(word):
# 	Palatalization (1)				k > tʃ, t > tʃ, s > ʃ			velar or alveolar to palato-alveolar before/after /i/ or /j/ or before front vowels
# 	Palatalization (2)				si > sji, li > lji				consonants are palatalized upon a condition
	return(word)

def phone_rasing(word,vowels=list(mid_vowels + close_mid_vowels + near_close_vowels + close_vowels)):										
																	# vowels is a list of one or more vowels (including category lists from "sounds.py")
# 	Phone Rasing					tet > tit						low or mid vowels raise to mid or high vowels
	for key in word.dict_stripped.keys():
		if word.dict_stripped[key] in vowels:
			v = raise_vowel(word.dict_stripped[key])
			word = change_sound(word,v,key)
	return(word)

def phone_lowering(word,vowels=list(open_vowels + near_open_vowels + open_mid_vowels + mid_vowels)):
																	# vowels is a list of one or more vowels (including category lists from "sounds.py")
# 	Phone Lowering					tut > tat						high or mid vowels lowering to mid or low vowels
	for key in word.dict_stripped.keys():
		if word.dict_stripped[key] in vowels:
			v = lower_vowel(word.dict_stripped[key])
			word = change_sound(word,v,key)
	return(word)

def nasalization(word):
# 	Nasalization					tan > tɑ̃n						nasalization of vowel before a nasal consonant
	return(word)

def compensatory_lengthening(word):
# 	Compensatory Lengthening		tast > ta:t						vowel lengthens to fill space from deletion
	return(word)

#####=====INSERTION=====#####################

def lengthening(word):
# 	Lengthening						tat > ta:t						some sound (usually a vowel) lengthens
	return(word)

def affrication(word):
# 	Affrication						ata > atʃa						consonant (usually a stop or fricative) becomes an affricate
	return(word)

def gemination(word):
#	Gemination						ata > atta						single consonant changes to a doubled consonant
	return(word)

def diphthongization(word):
# 	Diphthongization				tat > taut						single vowel becomes diphthong
	return(word)


#####=====DELETION=====######################

def deaffrication(word):
# 	Deaffrication					atʃa > aʃa						affricate becomes a fricative
	return(word)

def shortening(word):
# 	Shortening						ta:t > tat						some sound (usually a vowel) shortens
	return(word)

def degemination(word):
# 	Degemination					atta > ata						sequence of two identical consonants is reduced to a single consonant
	return(word)

def monophthongization(word):
# 	Monophthongization				taut > tat						diphthong becomes single vowel
	return(word)

def haplology(word):
# 	Haplology						kakasa > kasa					repeated sequence gets simplified
	return(word)


#####=====DELETION=====######################
#####=====OR CHANGE=====#####################

def fricativization(word):
# 	Spirantization 					atʃa > aʃa
# 	(Fricativization)				ata > asa						affricate or stop becomes a fricative
	return(word)
