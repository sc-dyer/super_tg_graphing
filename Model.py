#Class to open and manage an individual model
import csv
import os

class Model:
	PATH_FILE_NAME = "PTt-path.txt" #File name where the PTt path is stored
	GRT_FILE_PREF = "garnet_gen" #File prefix for the modelled compositions e.g "garnet_gen001a.txt"
	TEMP_COL = 0
	PRES_COL = 1
	TIM_COL = 2

	def __init__(self,dirIn,gen,trial):

		self.trial = -1 #Easy way to check if initialized
		self.gen = -1 #to use for checking if the gen exists for this trial

		if os.name == 'nt':#PC
			slash = "\\"
		else:#Mac
			slash= "/"

		#File paths for the PTt path and garnet composition
		pathDir = dirIn + slash + self.PATH_FILE_NAME
		grtDir = dirIn + slash + self.GRT_FILE_PREF + '{:03d}'.format(gen) + '.txt'



		try:
			pathFile = open(pathDir, 'r')
		except:
			print("PTt-path.txt for trial: " + str(trial) + " not found")
			return

		self.trial = trial

		try:
			grtFile = open(grtDir, 'r')
		except:
			print("Garnet generation: " + str(gen) + " not found in trial: " + str(trial))
			print("Please select different generation if you wish to include this trial")
			return

		self.gen = gen


		self.pressure = []
		self.temperature = []
		self.time = []

		#Read the PTt path
		line = pathFile.readline() #remove header
		line = pathFile.readline()
		while(len(line) > 0):
			items = [value.strip() for value in line.split()]
			self.temperature.append(float(items[self.TEMP_COL]))
			self.pressure.append(float(items[self.PRES_COL]))
			self.time.append(float(items[self.TIM_COL]))
			line = pathFile.readline()







		# self.pressure
		# self.temperature
		# self.time
		# self.x
		# self.mn
		# self.mg
		# self.fe
		# self.ca