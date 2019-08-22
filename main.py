#This is the main program for super_tg_graphing, see README


from Model import Model
from CompoProfile import CMPNT
from Traverse import Traverse
from ModelList import ModelList

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


	#Read through the driectory and collect each trial into ModelList
	myModels = ModelList(fileIn, gen)
	myModels.plotModels(trav,travSel)
	#Build the plots
	

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
			for i in range(len(myModels.models)):
				rowName = "Trial-" + str(i+1) +" (Right Half)"
				rightMatch = myModels.models[i].compareProfile(trav.travSplit[0],writeFile,rowName)

				if len(trav.travSplit) > 1:
					rowName = "Trial-" + str(i+1) + " (Left Half)"
					leftMatch = myModels.models[i].compareProfile(trav.travSplit[1],writeFile,rowName)
				else:
					leftMatch = float("inf") #So it doesnt meet conditional

				#Display the plots as green if they are good fits
				if rightMatch <= 0.1 or leftMatch <= 0.1:
					myModels.models[i].pltColour = 'green'


			writeFile.close()

			myModels.plotModels(trav,travSel)

		else:
			print("No output path chosen, ending program")
else:
	print('No model path chosen, ending program')


