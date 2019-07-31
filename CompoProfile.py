#General class to be extended by the Traverse class and the Model class
#Defines methods that can be used by any garnet composition profile
#Extended by Model and Traverse
import matplotlib.pyplot as plt
import os
import numpy as np
import pandas as pd

CMPNT = ["Mn","Mg","Ca","Fe"] #Components of garnet, this corresponds to the order they are placed in the cmpnts array

class CompoProfile:

	def __init__(self):

		#Empty initialization, defines the variables all CompoProfiles should have

		self.x = [] #distance in mm
		#mol fraction
		self.pltColour = 'black'
		self.pltLine = 'None'
		self.pltMark = 'None'
		self.cmpnts = [[],[],[],[]]#Array for mn,mg,ca,fe, each corresponds to a value in CMPNT
		


	def plotCompo(self, key, pltIn,mrkSize):
		#Plots the composition of a specific component in pltIn
		#input key should be one of the CMPNT
		#mrkSize input used for convenience when plotting things on different sized plots
		for i in range(len(CMPNT)):
			if(key==CMPNT[i]):
				yComp = self.cmpnts[i]
			
		
		pltIn.plot(self.x, yComp, color = self.pltColour, marker = self.pltMark, linestyle = self.pltLine, markersize = mrkSize, linewidth = 1, label = key)
	
	def getCmpnt(self, key):
		#Returns the array of whatever component was input to key
		#This is for user probing
		val = []
		for i in range(len(CMPNT)):
			if(key==CMPNT[i]):
				val = self.cmpnts[i]
		return val

	def compareProfile(self,compare):
		#Comparison must be another CompoProfile object
		#This method returns multiple r^2 values for all components or should it return average r^2
		#Assumes that these are two non-identical arrays CompoProfiles (e.g. a model and a traverse, or two different models)
		#Also assumes that both arrays start from core and go to the rim
		#Will take each x value of comparison and find what the composition should be at that x in "this"
		#Does this by finding the points at the two closest x values, calculates the line between the two points and plugs in the x value of the comparison
		#The intention is to compare a model profile to a half traverse, so it will interpolate values between points on the model for a least square regression
		
		for i in range(len(CMPNT)):
			thisCmpnt = []
			thatCmpnt = compare.cmpnts[i]

			for j in range(len(compare.x)):
				compotAtX = self.interpCompoAtX(compare.x[j],CMPNT[i])
				if compoAtX >= 0:
					thisCmpnt.append(compoAtX)




	def interpCompoAtX(self,xVal,key):
		#Linearly interpolate the composition between to points on the model to get the exact value at an x position

		count = 0
		while self.x[count] < xVal and count < len(self.x):
					count += 1

		compoAtX = -1 
		if count >= 0 and count <len(self.x):
			for i in range(len(CMPNT)):

				if CMPNT[i] == key:
					rightX = self.x[count]

					leftX = self.x[count-1]
				
					rightCmpnt = self.cmpnts[i][count]
					leftCmpnt = self.cmpnts[i][count-1]

					#linearly interpolate between two points and get the value at xVal
					slope = (rightCmpnt-leftCmpnt)/(rightX-leftX)
					midX = xVal - leftX
					compoAtX = midX*slope + leftCmpnt

		return compoAtX #Returns -1 if the first cell was to the right of the input xVal or if it is attempting to interpolate past the model size





