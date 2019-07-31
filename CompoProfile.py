#General class to be extended by the Traverse class and the Model class
#Defines methods that can be used by any garnet composition profile
#Extended by Model and Traverse
import matplotlib.pyplot as plt
import os
import numpy as np
import pandas as pd

CMPNT = ["Mn","Mg","Ca","Fe"] #Components of garnet, this corresponds to the order they are placed in the compnts array

class CompoProfile:

	def __init__(self):

		#Empty initialization, defines the variables all CompoProfiles should have

		self.x = [] #distance in mm
		#mol fraction
		self.pltColour = 'black'
		self.pltLine = 'None'
		self.pltMark = 'None'
		self.compnts = [[],[],[],[]]#Array for mn,mg,ca,fe, each corresponds to a value in CMPNT
		


	def plotCompo(self, key, pltIn,mrkSize):
		#Plots the composition of a specific component in pltIn
		#input key should be one of the CMPNT
		#mrkSize input used for convenience when plotting things on different sized plots
		for i in range(len(CMPNT)):
			if(key==CMPNT[i]):
				yComp = self.compnts[i]
			
		
		pltIn.plot(self.x, yComp, color = self.pltColour, marker = self.pltMark, linestyle = self.pltLine, markersize = mrkSize, linewidth = 1, label = key)
	
	def getCompnt(self, key):
		#Returns the array of whatever component was input to key
		#This is for user probing
		val = []
		for i in range(len(CMPNT)):
			if(key==CMPNT[i]):
				val = self.compnts[i]
		return val

	#def compareProfile(self,compare):
		#Comparison must be another CompoProfile object
		#This method returns multiple r^2 values for all components or should it 
		#Assumes that these are two non-identical arrays CompoProfiles (e.g. a model and a traverse, or two different models)
		#Also assumes that both arrays start from core and go to the rim
		#Will take each x value of comparison and find what the composition should be at that x in "this"
		#Does this by finding the points at the two closest x values, calculates the line between the two points and plugs in the x value of the comparison
		
			
	#def findCompoAtX(self,xVal,key):