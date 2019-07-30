#This is the main program for super_tg_graphing, see README

from Model import Model
from CompoProfile import CMPNT
from Traverse import Traverse
import os
import matplotlib.pyplot as plt
#import numpy as np

#GEN = 1



fileIn = input('Enter the directory where the SUPER_TG trials are stored: ')
fileIn = fileIn.strip()
fileIn = fileIn.strip('"')

travIn = input('Enter the name and directory of the csv file for the traverse: ')
travIn = travIn.strip()
travIn = travIn.strip('"')
#fileOut = input('Enter the desired directory for the output files to be saved (WARNING: THIS WILL OVERWRITE FILES OF THE SAME NAME, SAVE TO NEW FOLDER IF YOU DONT WANT THIS TO HAPPEN): ')
#fileOut = fileOut.strip()
#fileOut = fileOut.strip('"')

gen = int(input("Enter the garnet generation to plot: "))

#Make and plot the traverses
trav = Traverse(travIn)
travFig = plt.figure(figsize = (12,8))
travAx = travFig.add_subplot()

trav.plotAll(travAx)
print("Please click on the plot where you want to split it in half, if you are satisfied with the plot as is, exit the window")
plt.show()




#Read through the driectory and collect each trial into modelList
modelList = []
count = 1
currModel = Model(fileIn,gen,count)

#Continue loop until it reaches a trial number that doesnt exist
while(currModel.trial > 0):
    modelList.append(currModel)
    count += 1
    currModel = Model(fileIn,gen,count)
    
#Build the plots
modelFig = plt.figure(figsize =(16,10))
sbplot = 221 #location for first subplot
for i in range(len(CMPNT)):
    #Cycle through each component and graph the model output for each trial
    compoAx = modelFig.add_subplot(sbplot)
    
    for j in range(len(modelList)):
        modelList[j].plotCompo(CMPNT[i],compoAx,0)

    #Overlay the right and left halves of the traverse
    trav.rightTrav.plotCompo(CMPNT[i],compoAx,3)
    if(len(trav.leftTrav.x) > 0):
    	trav.leftTrav.plotCompo(CMPNT[i],compoAx,3)

    compoAx.set_xlabel("x (mm)")
    compoAx.set_ylabel("X (" + CMPNT[i] + ")")
    sbplot += 1

#Display the PT paths
pathFig = plt.figure(figsize = (12,8))
pathAx = pathFig.add_subplot()

for i in range(len(modelList)):
	modelList[i].pltPath(pathAx)

pathAx.set_xlabel("T (deg C)")
pathAx.set_ylabel("P (bar)")

plt.show()
