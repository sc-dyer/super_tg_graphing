#Class to open and manage an individual model
#import csv
import os
import numpy as np
import pandas as pd
from CompoProfile import CompoProfile
PATH_FILE_NAME = "PTt-path.txt" #File name where the PTt path is stored
GRT_FILE_PREF = "garnet_gen" #File prefix for the modelled compositions e.g "garnet_gen001a.txt"
TEMP_COL = 0
PRES_COL = 1
TIM_COL = 2

class Model(CompoProfile):

	
	def __init__(self,dirIn,gen,trial):

		self.trial = -1 #Easy way to check if initialized
		self.gen = -1 #to use for checking if the gen exists for this trial
		trialDir = 'Trial-' + '{:04d}'.format(trial)
		if os.name == 'nt':#PC
			slash = "\\"
		else:#Mac
			slash= "/"

		#File paths for the PTt path and garnet composition
		pathDir = dirIn + slash + trialDir + slash + PATH_FILE_NAME
		grtDir = dirIn + slash + trialDir + slash + GRT_FILE_PREF + '{:03d}'.format(gen) + 'a.txt'



		try:
			pathFile = open(pathDir, 'r')
		except:
			print("PTt-path.txt for trial: " + str(trial) + " not found at location:")
			print(pathDir)
			return

		self.trial = trial

		try:
			grtFile = open(grtDir, 'r')
		except:
			print("Garnet generation: " + str(gen) + " not found in trial: " + str(trial))
			print("Please select different generation if you wish to include this trial")
			return

		#grtFile.close()
		self.gen = gen


		self.pressure = []
		self.temperature = []
		self.time = []

		line = pathFile.readline() #remove header
		line = pathFile.readline()
		while(len(line) > 0):
			items = [value.strip() for value in line.split()]
			self.temperature.append(float(items[TEMP_COL]))
			self.pressure.append(float(items[PRES_COL]))
			self.time.append(float(items[TIM_COL]))

			line = pathFile.readline()

		pathFile.close()

		CompoProfile.__init__(self)



		#Read the garnet file, need to specifically take the last growth period, starts from the bottom and moves up
		#Header names are identical to output files from theriag, do not change these unless you change the theriag output as well
		grtdf = pd.read_csv(grtFile,)
		rowCount = grtdf.shape[0]
		shells = grtdf['shell     ']
		xCol = grtdf['node(cm)     ']
		mnCol = grtdf['x(Mn)     ']
		feCol = grtdf['x(Fe)     ']
		mgCol = grtdf['x(Mg)     ']
		caCol = grtdf['x(Ca)     ']
		row = rowCount-1


		#Will add the values from the corresponding columns then reverse them
		
		self.x.append(xCol[row])
		self.mn.append(mnCol[row])
		self.fe.append(feCol[row])
		self.mg.append(mgCol[row])
		self.ca.append(caCol[row])

		row-= 1

		while(shells[row] < shells[row+1]):
			self.x.append(xCol[row])
			self.mn.append(mnCol[row])
			self.fe.append(feCol[row])
			self.mg.append(mgCol[row])
			self.ca.append(caCol[row])
			#print(shells[row])
			row -= 1


		self.x.reverse()
		self.mn.reverse()
		self.fe.reverse()
		self.mg.reverse()
		self.ca.reverse()
		

		#print(self.rad)
		#print(self.mn)
		#for row in grtdf:

		# self.rad
		# self.mn
		# self.mg
		# self.fe
		# self.ca

	#def plot_comp