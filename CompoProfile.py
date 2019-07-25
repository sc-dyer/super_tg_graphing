#General class to be extended by the Traverse class and the Model class
#Defines methods that can be used by any garnet composition profile
#Possibly: include method for comparing profiles here?
import matplotlib.pyplot as plt
COMPS = ["Mn","Mg","Ca","Fe"]
class CompoProfile:

	def __init__(self):

		#Empty initialization, defines the variables all CompoProfiles should have

		self.x = [] #distance in mm
		#mol fraction
		self.mn = [] 
		self.mg = []
		self.ca = []
		self.fe = []
		self.pltColour = 'black'
		self.pltLine = 'None'
		self.pltMark = 'None'

	def plotCompo(self, key, pltIn):
		#Plots the composition of a specific component in pltIn
		#input key should be one of the COMPS
		
		if key == COMPS[0]:
			yComp = self.mn
		elif key == COMPS[1]:
			yComp = self.mg
		elif key == COMPS[2]:
			yComp = self.ca
		elif key == COMPS[3]:
			yComp = self.fe
			

		pltIn.plot(self.x, yComp, color = self.pltColour, marker = self.pltMark, linestyle = self.pltLine, markersize = 7, linewidth = 1)
		
	def compareProfile(self,comparison,key):
		#Comparison must be another CompoProfile object
		#This method returns an r^2 value which describes how well the two profiles match
		#Assumes that these are two non-identical arrays CompoProfiles (e.g. a model and a traverse, or two different models)
		#Also assumes that both arrays start from core and go to the rim
		#Will take each x value of comparison and find what the composition should be at that x in "this"
		#Does this by finding the points at the two closest x values, calculates the line between the two points and plugs in the x value of the comparison
		if key == COMPS[0]:
			thisVar = self.mn
			thatVar = comparison.mn
		elif key == COMPS[1]:
			thisVar = self.mg
			thatVar = comparison.mg
		elif key == COMPS[2]:
			thisVar = self.ca
			thatVar = comparison.ca
		elif key == COMPS[3]:
			thisVar = self.fe
			thatVar = comparison.fe
			
	#def findCompoAtX(self,xVal,key):
		