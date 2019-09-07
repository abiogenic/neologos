#!/usr/bin/env python3.7
# coding: utf-8
# dependences: pandas, numpy

#===================================================================================#
#=================================IMPORT MODULES====================================#
#===================================================================================#

# import random as rand
# import os
# from datetime import datetime, timedelta
import unicodedata

#===================================================================================#
#==================================DEPENDENCIES=====================================#
#===================================================================================#

# import pandas as pd
# import numpy as np
# from sounds import *
# from major_functions import *
# from global_settings import *

#===================================================================================#
#=====================================CLASSES=======================================#
#===================================================================================#

# class Phone:
# 	def __init__(self,symbol):


class Word:
	def __init__(self,string):
		self.string = string
	def __str__(self):
		return str(self.string[1:-1])
		

#===================================================================================#
#===================================DEFINTIONS======================================#
#===================================================================================#

# home_dir = str(os.getcwd() + "/..")
# input_dir = home_dir + "/input"

# ipa = pd.read_csv(str(input_dir+"/"+ipa_file_name), engine="python", encoding="UTF-16", sep="\t", index_col=0)
# ipa = ipa.fillna('0')

# ipa_dict = dict()

# for i in ipa.index:
# 	ipa_dict[i] = Phone(i)

