#!/usr/bin/env python3
# coding: utf-8
# dependences: none

#===================================================================================#
#=====================================SETTINGS======================================#
#===================================================================================#

words_to_create = 20			# any integer
stress_feet = 'l'				# 'l' or 'r' or 'm' if foot_max == 3
build_feet = 'r'				# 'l' or 'r'
main_stressed_foot = 'l'		# 'l' or 'r' or int <= min_len/foot_max -1
syllabic_consonant_freq = 0.0	# float 0.0 - 1.0
complex_onsets_freq = 0.0		# float 0.0 - 1.0
complex_nucleus_freq = 0.0		# float 0.0 - 1.0
coda_frequency = 0.2			# float 0.0 - 1.0
geminate_freq = 0.2				# float 0.0 - 1.0
min_len = 2						# any integer <= max_len
max_len = 3						# any integer >= min_len
foot_max = 2					# any integer (ideally 2 or 3)

file_name = 'inventory_4th.csv'
ipa_file_name = 'ipa.csv'

onsets = ["p","m","t","n","r","s","l","c","k","j","ç","ʀ"]
geminate_consonants = ["pp","tt","kk","cc"]
complex_onsets = ["pl","ts","cç","ln","ps"]
nuclear_vowels = ["i","a","u","o","ɛ"]
diphthongs = ["ai","au","aː","iu","ia","iː","ua","ui","uː","ɛː"]
codas = ["p","m","t","n","r","s","l","c","k","j","ɱ","ɳ","ŋ","ç","ʀ"]
syllabic_consonants = ["m","n","l","ɱ","ɳ","ŋ"]

fix_randomization = True		# boolean (set to True to set seed)
seed_variable = 2				# any integer, even if fix_randomization is False

#===================================================================================#
#=====================================CHANGES=======================================#
#===================================================================================#

# insert, change, delete
# insertions.initial(word,'n')

