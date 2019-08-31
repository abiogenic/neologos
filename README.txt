                              ,,                                      
                            `7MM                                      
                              MM                                      
`7MMpMMMb.  .gP"Ya   ,pW"Wq.  MM  ,pW"Wq.   .P"Ybmmm ,pW"Wq.  ,pP"Ybd 
  MM    MM ,M'   Yb 6W'   `Wb MM 6W'   `Wb :MI  I8  6W'   `Wb 8I   `" 
  MM    MM 8M"""""" 8M     M8 MM 8M     M8  WmmmP"  8M     M8 `YMMMa. 
  MM    MM YM.    , YA.   ,A9 MM YA.   ,A9 8M       YA.   ,A9 L.   I8 
.JMML  JMML.`Mbmmd'  `Ybmd9'.JMML.`Ybmd9'   YMMMMMb  `Ybmd9'  M9mmmP' 
                                           6'     dP                  
                                           Ybmmmd'     

neologos: a python package create and evolve words for a new or existing conlang. 

Users modify the global_settings.py file to set parameters and phones for the words that will be created.
Options cover: 
    number of words being generated, 
    size of words (in syllables),
    frequencies of syllable components, 
    stress properties
   


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

Based off an early project:

Package has functionality to read .csv dataframes of words, translations, etc and to transcribe them (although for some languages this is a beast in and of itself so I may remove this for languages that donʼt have easy 1-to-1 ipa to orthography correspondents).

Hereʼs an example of the input, from which a script randomly draws an affix and a root word that will work with it, and organizes them in the correct order. Then the package can be called to analyze this new word.

And here is a result of a script that does this four times and analyzes the new words to count the violations of constraints I have specified:
 
If these violate any constraints, they need other possible candidates to compete with, so thatʼs the next step. I have some reading to do to determine a reasonable minimum number of candidates to go through these constraints and still determine a winner while using a reasonable amount of computational power. Below is the guts of the vowel_harmony function which when called will default to matching all three parameters unless otherwise specified. Its input is a string of IPA objects and its output is simply an integer count of how many times this rule was violated by this string.

For now the order in which the script calls the packageʼs constraints is hard-coded, but it will soon take a config.txt file where the user can list constraints to be judged, as well as the location for the language data.
