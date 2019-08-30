#!/usr/bin/env python3

import os
import copy
import glob
import shutil
import random
from datetime import datetime, timedelta
from operator import *

runOver = False
runOnce = False
run = True
showStatus = False
extendedOutput = True
repeat = True


""" USER CAN SET THESE """

mt_min_location = 244926
mt_max_location = 1000000

cp_min_location = 129500
cp_max_location = 1000000

home_dir = str(os.getcwd() + "/..")
os.chdir(home_dir)

input_dir = home_dir + "/input"
output_dir = home_dir + "/output"
scripts_dir = home_dir + "/scripts"
organelles = ["mt","cp"]

""" DO NOT ALTER BELOW THIS LINE """
day = datetime.now()
timestamp = str(day)
timestamp = timestamp.split()
current_date = timestamp[0]
# current_time = timestamp[1].split(":")
# current_hour = current_time[0]
# current_min = current_time[1]

if runOver:								# THIS SHORTENS CSVs AND CREATES VCFs IF RUNOVER

	for organelle in organelles:		# THIS RUNS ONCE FOR EACH ORGANELLAR GENOME

		# PREP DIRECTORIES FOR THIS ORGANELLE
		
		input_dir_current = str(input_dir + "/" + organelle + "_csv")
		output_dir_current = str(output_dir + "/" + organelle + "/" + current_date)

		try:	# check if input directory exists
			os.path.exists(input_dir_current)
		except:
			quit()

		try:	# create output directory
			os.makedirs(output_dir_current, exist_ok=True)
		except:
			print(str("Cannot create output directory " + output_dir_current))
			quit()

		# CHANGE TO SCRIPTS_DIR AND RUN SHORTEN_CSVS

		os.chdir(scripts_dir)
		import shorten_csvs
		print("\t>> shorten_csvs.py for " + organelle)
		if organelle == 'mt':
			shorten_csvs.main(input_dir_current,output_dir_current,mt_min_location,mt_max_location)
		elif organelle == 'cp':
			shorten_csvs.main(input_dir_current,output_dir_current,cp_min_location,cp_max_location)

		# CHANGE TO SCRIPTS_DIR AND RUN CREATE_VCFS

		os.chdir(scripts_dir)
		import create_vcfs
		if runOver:
			print("\t>> create_vcfs.py for " + organelle)
			create_vcfs.main(input_dir_current,output_dir_current)

else:
	anteday = day
	date_not_found = 1
	while date_not_found:
		timestamp = str(anteday)
		timestamp = timestamp.split()
		current_date = timestamp[0]
		output_dir_current = str(output_dir + "/" + organelles[0] + "/" + current_date)
		try:	# check if input directory exists
			if os.path.exists(output_dir_current):
				date_not_found = 0
		except:
			pass
		anteday = anteday - timedelta(days=1)

#for organelle in ['mt']:		# THIS RUNS ONCE FOR EACH ORGANELLAR GENOME
for organelle in organelles:		# THIS RUNS ONCE FOR EACH ORGANELLAR GENOME

	# CHANGE TO SCRIPTS_DIR AND RUN POLYPLOID_NORMALIZED
	os.chdir(scripts_dir)
	import haplotype_parser
	print("\t>> haplotype_parser.py for " + organelle)
	output_dir_current = str(output_dir + "/" + organelle + "/" + current_date)
	haplotype_parser.main(output_dir_current,repeat,organelle)

