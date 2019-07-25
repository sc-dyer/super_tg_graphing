#This is a program to plot the output of SUPER_TG and compare it to
#traverses measured in real samples


from Model import Model
from CompoProfile import COMPS
import os
import matplotlib.pyplot as plt
#import numpy as np

GEN = 1



fileIn = input('Enter the directory where the SUPER_TG trials are stored: ')
fileIn = fileIn.strip()
fileIn = fileIn.strip('"')


#fileOut = input('Enter the desired directory for the output files to be saved (WARNING: THIS WILL OVERWRITE FILES OF THE SAME NAME, SAVE TO NEW FOLDER IF YOU DONT WANT THIS TO HAPPEN): ')
#fileOut = fileOut.strip()
#fileOut = fileOut.strip('"')

modelList = []
count = 1
currModel = Model(fileIn,GEN,count)

while(currModel.trial > 0):
    modelList.append(currModel)
    count += 1
    currModel = Model(fileIn,GEN,count)
    
sbplot = 221 #location for first subplot
for i in range(len(COMPS)):
    #Cycle through each component and graph the model output for each trial

    plt.subplot(sbplot)
    for j in range(len(modelList)):
        modelList[j].plotCompo(COMPS[i],plt)
    plt.xlabel("x (mm)")
    plt.ylabel("X (" + COMPS[i] + ")")
    sbplot += 1


plt.show()

