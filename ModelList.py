#Class for working with a collection of models


from Model import Model
from CompoProfile import CMPNT
from Traverse import Traverse

import os
import matplotlib.pyplot as plt

class ModelList:

	def __init__(self,readDir,genIn):
		#Only one variable, list of models

		self.models = []
		count = 1
		currModel = Model(readDir,genIn,count)

		#Continue loop until it reaches a trial number that doesnt exist
		while(currModel.trial > 0):
			self.models.append(currModel)
			count += 1
			currModel = Model(readDir,genIn,count)


	def plotModels(self,travIn,travSelIn):
		#Build the plots
		#Plot all models, with traverses if there are any
		modelFig = plt.figure(figsize =(16,10))
		sbplot = 221 #location for first subplot
		for i in range(len(CMPNT)):
			#Cycle through each component and graph the model output for each trial
			compoAx = modelFig.add_subplot(sbplot)

			for j in range(len(self.models)):
				self.models[j].plotCompo(CMPNT[i],compoAx,0)

			#Overlay the right and left halves of the traverse
			if travSelIn:
				tSplit = travIn.travSplit
				for j in range(len(tSplit)):
					tSplit[j].plotCompo(CMPNT[i],compoAx,3)
				
			compoAx.set_xlabel("x (mm)")
			compoAx.set_ylabel("X (" + CMPNT[i] + ")")
			sbplot += 1

		#Display the PT paths
		pathFig = plt.figure(figsize = (12,8))
		pathAx = pathFig.add_subplot()

		for i in range(len(self.models)):
			self.models[i].pltPath(pathAx)

		pathAx.set_xlabel("T (deg C)")
		pathAx.set_ylabel("P (bar)")

		plt.show()