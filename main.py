#This is the main program for super_tg_graphing, see README


from Model import Model
from CompoProfile import CMPNT
from Traverse import Traverse

import os
import matplotlib.pyplot as plt
import easygui



print('Choose the csv file for the traverse')
#travIn = input('Enter the name and directory of the csv file for the traverse: ')
travIn = easygui.fileopenbox('Choose the csv file for the traverse')
if travIn != None:
	travIn = travIn.strip()
	travIn = travIn.strip('"')



	#gen = int(input("Enter the garnet generation to plot: "))

	#Make and plot the traverses
	trav = Traverse(travIn)
	travFig = plt.figure(figsize = (12,8))
	travAx = travFig.add_subplot()

	trav.plotAll(travAx)
	print("Please click on the plot where you want to split it in half, if you are satisfied with the plot as is, exit the window")
	plt.show()
	travSel = True
else:
	print("No csv file chosen, continuing without")
	travSel = False

print('Choose the directory where the SUPER_TG trials are stored')

#Start plotting things from a super_tg model directory
fileIn = easygui.diropenbox("Choose the directory where the SUPER_TG trials are stored ")
if fileIn != None:
	fileIn = fileIn.strip()
	fileIn = fileIn.strip('"')

	msg = "Enter the generation of garnet you wish to plot"
	gen = easygui.integerbox(msg)


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
	    if travSel:
	    	tSplit = trav.travSplit
	    	for j in range(len(tSplit)):
	    		tSplit[j].plotCompo(CMPNT[i],compoAx,3)
	    		
		    

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

	#Output the mean squared error stuff
	if travSel:

		print("Create a file where you would like to store the output")
		fileOut = easygui.filesavebox("Create a file where you would like to store the output")
		if fileOut != None:
			try: 
				writeFile = open(fileOut, 'w')
			except:
				print('Problem creating new file')
				exit(0)
				
			#write the header
			header = "Model,"
			for i in range(len(CMPNT)):
				header += "RMSE(" + CMPNT[i] + "),"
			header += "RMSE(Average),"
			for i in range(len(CMPNT)):
				header += "NRMSE("+CMPNT[i] + "),"
			header += "NRMSE(Average)\n"

			writeFile.write(header)

			#Compare the model to each half of the traverse for each model
			for i in range(len(modelList)):
				rowName = "Trial-" + str(i+1) +" (Right Half)"
				modelList[i].compareProfile(trav.travSplit[0],writeFile,rowName)

				if len(trav.travSplit) > 1:
					rowName = "Trial-" + str(i+1) + " (Left Half)"
					modelList[i].compareProfile(trav.travSplit[1],writeFile,rowName)

			writeFile.close()

		else:
			print("No output path chosen, ending program")
else:
	print('No model path chosen, ending program')