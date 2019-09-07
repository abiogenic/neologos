#!/usr/bin python3.7
# coding: utf-8
# dependences: pandas, numpy

#===================================================================================#
#=================================IMPORT MODULES====================================#
#===================================================================================#

import random as rand
import os
from datetime import datetime, timedelta
import unicodedata

wd = os.getcwd()

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

if needs_dependency:
	quit()

#===================================================================================#
#==================================SETTINGS CHECK===================================#
#===================================================================================#

from global_settings import *

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
#=====================================CLASSES=======================================#
#===================================================================================#

class Word:

	def __init__(self,dictionary):
		self.dictionary = dictionary

	# class Syllable:
	# 	def __init__(self,syllables):
	# 		self.syllables = syllables

	# 	def __init__(self,syllables):
	# 		self.Syllable(syllables)

#===================================================================================#
#==================================FUNCTION CALLS===================================#
#===================================================================================#

os.chdir(output_dir)
# words = create_words()
words = [{0:('m',''),1:('ɛ','ː')}]
for word in words:
	word = Word(word)
	print(word.dictionary)




