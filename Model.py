#Class to open and manage an individual model 
import csv
import os

class Model:
	PATH_FILE_NAME = "PTt-path.txt" #File name where the PTt path is stored
	GRT_FILE_PREF = "garnet_gen" #File prefix for the modelled compositions e.g "garnet_gen001a.txt"

	def __init__(self,dirIn,gen,trial):

		self.trial = -1 #Easy way to check if initialized
		self.gen = -1 #to use for checking if the gen exists for this trial

		if os.name == 'nt':#PC
			slash = "\\"
		else:#Mac
			slash= "/"

		#File paths for the PTt path and garnet composition
		pathDir = dirIn + slash + PATH_FILE_NAME
		grtDir = '%(directory)%(slash)%(fileName)%(generation)03d.txt' % \
			{"directory":dirIn,"slash":slash,"fileName":GARNET_FILE_PREF,"generation":gen}

		
		try:
			pathFile = open(pathDir, 'r')
		except:
			print("PTt-path.txt for trial: " + trial + " not found")
			return

		self.trial = trial

		try:
			grtFile = open(grtDir, 'r')
		except:
			print("Garnet generation: " + gen + " not found in trial: " + trial)
			print("Please select different generation if you wish to include this trial")
			return

		self.gen = gen
		





		# self.pressure
		# self.temperature
		# self.time
		# self.x
		# self.mn 
		# self.mg 
		# self.fe
		# self.ca 