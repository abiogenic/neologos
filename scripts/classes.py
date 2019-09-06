#!/usr/bin/env python3.7
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
from sounds import *
from functions import *
from global_settings import *

#===================================================================================#
#=====================================CLASSES=======================================#
#===================================================================================#

class Phone:
	def __init__(self,symbol):
		self.array = ipa.loc[symbol]
		self.symbol, self.type, self.voicing, self.place, self.subplace, self.manner, self.submanner, self.laterality, self.liquidity, self.stridency, self.sibilance, self.roundedness, self.height, self.backness, self.sonority = symbol, self.array['type'], self.array['voicing'], self.array['place'], self.array['subplace'], self.array['manner'], self.array['submanner'], self.array['laterality'], self.array['liquidity'], self.array['stridency'], self.array['sibilance'], self.array['roundedness'], self.array['height'], self.array['backness'], self.array['sonority']
		self.dictionary = {'symbol':self.symbol, 'type':self.type, 'voicing':self.voicing, 'place':self.place, 'subplace':self.subplace, 'manner':self.manner, 'submanner':self.submanner, 'laterality':self.laterality, 'liquidity':self.liquidity, 'stridency':self.stridency, 'sibilance':self.sibilance, 'roundedness':self.roundedness, 'height':self.height, 'backness':self.backness, 'sonority':self.sonority}
	
	def __str__(self):
		return str(self.symbol)

	def __repr__(self):
		return str(self.symbol)

class Word:
	def __init__(self,string):
		
		unicode_letters, unicode_diacritics = sounds.find_diacritics(sample_string)

		string = "[" + string + "]"
		self.dict = {i:string[i] for i in range(0,len(string))}
		
		self.dict_stripped = copy.deepcopy(self.dict)
		self.dict_stripped_diacritics = copy.deepcopy(self.dict)
		for key in self.dict.keys():
			if self.dict[key] in ["[",".","]","|","ˈ","ˌ"]:
				del self.dict_stripped[key]
				del self.dict_stripped_diacritics[key]
			elif self.dict[key] in unicode_diacritics:
				del self.dict_stripped_diacritics[key]

		self.string = str()
		for i in self.dict.values():
			self.string = str(self.string + str(i))

		self.string_stripped = str()
		for i in self.dict_stripped.values():
			self.string_stripped = str(self.string_stripped + str(i))

		self.string_stripped_diacritics = str()
		for i in self.dict_stripped_diacritics.values():
			self.string_stripped_diacritics = str(self.string_stripped_diacritics + str(i))
		
		self.syllables = []
		self.feet = []
		for foot in [i.strip(".") for i in self.string.split("|")]:
			self.feet.append(foot.split("."))
		for foot in self.feet:	
			for syllable in foot:
				self.syllables.append(syllable.strip("."))

	def __str__(self):
		return str(self.string[1:-1])

	def __len__(self):
		return len(self.syllables)

	def __getitem__(self,index):
		return [i for i in self.string]

#===================================================================================#
#===================================DEFINTIONS======================================#
#===================================================================================#

home_dir = str(os.getcwd() + "/..")
input_dir = home_dir + "/input"

ipa = pd.read_csv(str(input_dir+"/"+ipa_file_name), engine="python", encoding="UTF-16", sep="\t", index_col=0)
ipa = ipa.fillna('0')

ipa_dict = dict()

for i in ipa.index:
	ipa_dict[i] = Phone(i)

