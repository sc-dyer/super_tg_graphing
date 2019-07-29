#Class to open and manage the measured garnet traverse
#Must be in a csv file with the following header:
#x (mm),Ca,Mg,Fe,Mn 
#The unit for components should be mol fraction
import matplotlib.pyplot as plt
import os
import numpy as np
import pandas as pd

from CompoProfile import CompoProfile, COMPS

class Traverse(CompoProfile):

	def __init__(self, fileName):
		#Read the file containg probe data and store it in this object
		CompoProfile.__init__(self)
		self.pltMark = 'o'

		#open the csv file
		try:
			grtFile = open(fileName, 'r')
		except:
			print("No csv file found at location:")
			print(fileName)
			return
		
		grtdf = pd.read_csv(grtFile)
		self.x = grtdf['x (mm)']
		self.ca = grtdf['Ca']
		self.mg = grtdf['Mg']
		self.fe = grtdf['Fe']
		self.mn = grtdf['Mn']

	def plotAll(self, pltIn):
		#Method to plot all components on one plot
		colours = ['green','blue','orange','red']
		pltAlm = pltIn.twinx()
		

		for i in range(len(COMPS)):
			self.pltColour = colours[i]
			if(COMPS[i] == "Fe"):
				CompoProfile.plotCompo(self,COMPS[i],pltAlm)
			else:
				CompoProfile.plotCompo(self,COMPS[i],pltIn)

		pltIn.set_xlabel("x (mm)")
		pltIn.set_ylabel("X (Ca,Mn,Mg)")
		pltAlm.set_ylabel("X (Fe)")
		pltIn.legend(fontsize = 14, loc = 'upper left')
		pltAlm.legend(fontsize = 14, loc = 'upper right')

	def splitTrav(self,xPos):
		#Method for splitting the traverse into two halves at the inputted xPos
		