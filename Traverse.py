#Class to open and manage the measured garnet traverse
#Must be in a csv file with the following header:
#x (mm),Ca,Mg,Fe,Mn 
#The unit for components should be mol fraction
#This class is an extension of CompoProfile
import matplotlib.pyplot as plt
import os
import numpy as np
import pandas as pd
import easygui

from CompoProfile import CompoProfile, CMPNT

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
		for i in range(len(CMPNT)):
			self.compnts[i] = list(grtdf[CMPNT[i]])
		

	def plotAll(self, pltIn):
		#Method to plot all components on one plot
		#Assumes that the Fe component is much higher than the rest, plots it on seperate axis
		colours = ['green','blue','orange','red']
		pltAlm = pltIn.twinx()
		
		self.travPlot = pltIn #Saves the plot to the object

		#Loop for plotting
		for i in range(len(CMPNT)):
			self.pltColour = colours[i]
			if(CMPNT[i] == "Fe"):
				CompoProfile.plotCompo(self,CMPNT[i],pltAlm,7)
			else:
				CompoProfile.plotCompo(self,CMPNT[i],pltIn,7)

		pltIn.set_xlabel("x (mm)")
		pltIn.set_ylabel("X (Ca,Mn,Mg)")
		pltAlm.set_ylabel("X (Fe)")
		pltIn.legend(fontsize = 14, loc = 'upper left')
		pltAlm.legend(fontsize = 14, loc = 'upper right')

		#This is to set up the stuff for splitting the plot in half, assuming that you input a full traverse instead of a half traverse
		self.cid = pltIn.figure.canvas.mpl_connect('button_press_event',self.travClick)
		self.splitLine = pltIn.plot([0],[0]) #create an empty line
		self.splitTrav(-1)#Sets the baseline to leftTrav is empty and rightTrav = this. This is basically if you want to input just a half traverse, however it assumes that it is the right half

	def travClick(self, event):
		#When the plot is clicked, draw a vertical line where clicked and store that value as the new 0 for splitting the traverse
		#Will ask for confirmation before drawing and storing the location.
		#It can be changed as many times as desired
		self.splitLine.pop(0).remove()
		newZero = event.xdata
		self.travPlot.autoscale(False)
		self.splitLine = self.travPlot.plot([newZero,newZero],[-100,100],color = 'black',linestyle = '--')
		
		
		a = 0
		title = ""
		msg = "Split traverse at x = " + str(newZero) + "?"
		answer = easygui.boolbox(msg,title,["Yes","No"])
		#answer = input('Split traverse at x = ' + str(newZero) +'? (y/n)')
		if answer:
			self.splitTrav(newZero)
			plt.draw()
			print("Done, you may now exit this plot or choose a different x location to split the traverse.")

		

	def splitTrav(self,xPos):
		#Method for splitting the traverse into two halves at the inputted xPos
		#Assumes xpos will never exactly equal to an x position on the traverse
		#The two halves are CompoProfile objects with the same data of their respective halves of this Traverse object. 
		#They will contain a little less info but maintain most of the core stuff
		count = 0
		#Finds the index of the datapoint to the right of the selected x
		while(self.x[count] < xPos):
			count+=1


		xRightIndex = count

		xLeftIndex = count - 1

		self.rightTrav = CompoProfile()
		self.leftTrav = CompoProfile()
		self.rightTrav.pltMark = 'o'
		self.leftTrav.pltMark = 'o'
		self.leftTrav.pltColour = 'blue' #So it can be differentiated on the plot

		#Build the contained arrays
		for i in range(xRightIndex,len(self.x)):
			
			self.rightTrav.x.append(self.x[i] - xPos)
			for j in range(len(CMPNT)):
				self.rightTrav.compnts[j].append(self.compnts[j][i])
			

		#Flips the left Traverse
		for i in range(xLeftIndex,-1,-1):
			self.leftTrav.x.append(xPos - self.x[i])
			for j in range(len(CMPNT)):
				self.leftTrav.compnts[j].append(self.compnts[j][i])
	



